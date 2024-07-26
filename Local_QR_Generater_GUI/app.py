import os
from PIL import Image
from flask import Flask, send_file, jsonify, request, abort
import qrcode
import time

app = Flask(__name__)

# 상대 경로 설정
IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), 'origin_img')
QR_FOLDER = os.path.join(os.path.dirname(__file__), 'QR_img')
WATERMARKED_FOLDER = os.path.join(os.path.dirname(__file__), 'watermarked_img')

# 공인 IP 주소를 수동으로 설정 (라우터 설정에서 확인 가능)
PUBLIC_IP = '172.20.10.3'

# QR 코드 생성 함수
def generate_qr_code(data, qr_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_path)

# 워터마크 추가 함수
def add_qr_watermark(image_path, qr_path, output_path):
    base_image = Image.open(image_path)
    qr_image = Image.open(qr_path)

    # QR 코드 크기 조절 (원본 이미지의 10% 크기로 조정)
    base_width, base_height = base_image.size
    qr_size = int(min(base_width, base_height) * 0.3)
    qr_image = qr_image.resize((qr_size, qr_size))

    # QR 코드를 원본 이미지의 오른쪽 아래에 추가
    position = (base_width - qr_size - 10, base_height - qr_size - 10)
    base_image.paste(qr_image, position, qr_image.convert("RGBA"))

    base_image.save(output_path)

def generate_qrs():
    if not os.path.exists(QR_FOLDER):
        os.makedirs(QR_FOLDER)
    if not os.path.exists(WATERMARKED_FOLDER):
        os.makedirs(WATERMARKED_FOLDER)

    image_files = [f for f in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, f))]
    qr_files = []

    for image_file in image_files:
        image_path = os.path.join(IMAGE_FOLDER, image_file)
        watermarked_filename = f"{os.path.splitext(image_file)[0]}_watermarked.png"
        watermarked_path = os.path.join(WATERMARKED_FOLDER, watermarked_filename)
        
        # 워터마크된 이미지에 대한 URL 생성
        watermarked_url = f"http://{PUBLIC_IP}:5000/watermarked_images/{watermarked_filename}"
        
        # 워터마크된 이미지에 대한 QR 코드 생성
        qr_filename = f"{os.path.splitext(image_file)[0]}_qr.png"
        qr_path = os.path.join(QR_FOLDER, qr_filename)
        generate_qr_code(watermarked_url, qr_path)
        
        # 원본 이미지에 QR 코드를 워터마크로 추가
        add_qr_watermark(image_path, qr_path, watermarked_path)
        
        qr_files.append(qr_filename)
    
    return qr_files

# 허용된 IP 목록
ALLOWED_IPS = ['허용 IP'] 

def require_ip(func):
    def wrapper(*args, **kwargs):
        if request.remote_addr not in ALLOWED_IPS:
            abort(403, description="Forbidden")
        return func(*args, **kwargs)
    return wrapper

# 요청 제한을 위한 데이터 저장소 (메모리, 파일, 데이터베이스 등)
rate_limit = {}

def rate_limit_check(func):
    def wrapper(*args, **kwargs):
        client_ip = request.remote_addr
        now = time.time()
        if client_ip in rate_limit:
            last_request_time = rate_limit[client_ip]
            if now - last_request_time < 10:  # 1분 내에 요청이 너무 많으면 차단
                abort(429, description="Too Many Requests")
        rate_limit[client_ip] = now
        return func(*args, **kwargs)
    return wrapper

@app.route('/generate_qr', methods=['GET'])
@rate_limit_check
# @require_ip
def generate_qr_endpoint():
    qr_files = generate_qrs()
    return jsonify({"qr_codes": qr_files}), 200

# # 이미지 파일을 제공하는 엔드포인트
# @app.route('/images/<filename>', methods=['GET'])
# def get_image(filename):
#     image_path = os.path.join(IMAGE_FOLDER, filename)
#     if not os.path.exists(image_path):
#         return jsonify({"error": "Image not found"}), 404

#     return send_file(image_path, mimetype='image/png')

# 워터마크 이미지를 제공하는 엔드포인트
@app.route('/watermarked_images/<filename>', methods=['GET'])
def get_watermarked_image(filename):
    image_path = os.path.join(WATERMARKED_FOLDER, filename)
    if not os.path.exists(image_path):
        return jsonify({"error": "Image not found"}), 404

    return send_file(image_path, mimetype='image/png')

# QR 코드 이미지를 제공하는 엔드포인트
@app.route('/qr_codes/<filename>', methods=['GET'])
def get_qr_code(filename):
    qr_path = os.path.join(QR_FOLDER, filename)
    if not os.path.exists(qr_path):
        return jsonify({"error": "QR code not found"}), 404

    return send_file(qr_path, mimetype='image/png')

if __name__ == '__main__':
    # 서버 시작 시 QR 코드 생성
    generate_qrs()
    app.run(debug=True, host='0.0.0.0', port=5000)
