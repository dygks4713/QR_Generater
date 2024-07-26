# QR Code Generater

- 이 프로젝트는 명함 이미지 파일에 QR 코드를 생성하고 워터마크로 추가하는 기능 제공 
- 사용자는 원본 명함 이미지를 업로드하고, QR 생성하면 생성된 QR 코드와 워터마크가 포함된 이미지 확인 가능 
- 클라우드타입 클라우드 서버를 이용하여 외부 네트워크에서도 QR코드 인식하면 워터마크가 포함된 이미지 확인 가능
- 로컬 환경에서 Flask 웹 서버를 통해 이미지 파일과 QR 코드를 호스팅 가능

------------

## 주요 기능

- 이미지 파일에서 QR 코드를 생성하고 워터마크로 추가
- Flask 웹 서버를 통한 이미지 및 QR 코드 파일 호스팅
- Tkinter GUI를 통해 서버 시작 및 QR 코드 생성 관리
- 원본 이미지 폴더와 QR 코드 폴더를 쉽게 열 수 있는 기능

------------

# Install and Build
    git clone https://github.com/dygks4713/QR_Generater.git
## Python 라이브러리 설치
    pip install -r requirements.txt

------------

# Cloudtype_QR_Generater_Web
- Cloudtype 클라우드 서버를 이용
- 서버를 실행후 https://부여받은 서버 주소/generate_qr 링크 입력하면 QR 이미지 생성
- QR 확인 방법은 https://부여받은 서버 주소/qr_codes/파일 이름
- 명함에 QR코드가 적용된 이미지 확인 방법 https://부여받은 서버 주소/watermarked_images/파일 이름

# Local_QR_Generater_GUI
- 터미널에서 python app.py 입력
- GUI 환경에서 로컬 환경에서 Flask 웹서버 실행 및 QR 생성, QR코드 확인, QR코드 적용된 명함 이미지 확인 가능

# 라이브러리 라이선스
이 프로젝트는 다음 라이브러리들을 사용합니다:

- **Flask**:
  - 라이선스: BSD License
  - [라이선스 문서](https://opensource.org/licenses/BSD-3-Clause)
  - 설명: BSD 라이선스는 상업적 사용을 포함하여 자유롭게 소스 코드를 사용하고 수정할 수 있도록 허용합니다.

- **qrcode**:
  - 라이선스: MIT License
  - [라이선스 문서](https://opensource.org/licenses/MIT)
  - 설명: MIT 라이선스는 소스 코드의 사용, 수정, 배포를 자유롭게 허용합니다.

- **Pillow**:
  - 라이선스: PIL Software License
  - [라이선스 문서](https://pillow.readthedocs.io/en/stable/releasenotes/2.0.0.html#license)
  - 설명: Pillow는 PIL의 후속 라이브러리로, 대부분의 경우 상업적 사용이 가능합니다.

- **requests**:
  - 라이선스: Apache License 2.0
  - [라이선스 문서](https://opensource.org/licenses/Apache-2.0)
  - 설명: Apache License 2.0은 상업적 사용을 허용하며, 라이선스의 조건에 따라 저작권 및 라이선스 정보를 유지해야 합니다.

- **Tkinter**:
  - 라이선스: Python License
  - [라이선스 문서](https://docs.python.org/3/license.html)
  - 설명: Tkinter는 Python의 표준 라이브러리로 포함되어 있으며, Python 라이선스는 상업적 사용을 제한하지 않습니다.

이 프로젝트는 위 라이브러리들의 라이선스를 준수합니다. 라이선스의 세부 사항은 각 링크에서 확인할 수 있습니다.
