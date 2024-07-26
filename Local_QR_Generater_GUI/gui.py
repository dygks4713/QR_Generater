import tkinter as tk
from tkinter import messagebox
import subprocess
import requests
import os

# Flask 서버를 백그라운드에서 실행하는 함수
def start_server():
    try:
        subprocess.Popen(['python', 'app.py'])
        messagebox.showinfo("서버 시작", "서버가 성공적으로 시작되었습니다.")
    except Exception as e:
        messagebox.showerror("서버 시작 오류", str(e))

# QR 코드 생성 요청을 보내는 함수
def generate_qr_codes():
    try:
        response = requests.get('http://127.0.0.1:5000/generate_qr')
        if response.status_code == 200:
            qr_codes = response.json().get("qr_codes", [])
            messagebox.showinfo("QR 코드 생성 완료", f"{len(qr_codes)}개의 QR 코드가 생성되었습니다.")
        else:
            messagebox.showerror("QR 코드 생성 오류", response.text)
    except Exception as e:
        messagebox.showerror("QR 코드 생성 오류", str(e))

# QR 코드 이미지 폴더를 여는 함수
def open_qr_folder():
    qr_folder = os.path.join(os.path.dirname(__file__), 'QR_img')
    try:
        os.startfile(qr_folder)
    except Exception as e:
        messagebox.showerror("폴더 열기 오류", str(e))

# 원본 이미지 폴더를 여는 함수
def open_origin_img_folder():
    origin_img_folder = os.path.join(os.path.dirname(__file__), 'origin_img')
    try:
        os.startfile(origin_img_folder)
    except Exception as e:
        messagebox.showerror("폴더 열기 오류", str(e))

# QR 코드 추가된 이미지 폴더를 여는 함수
def open_watermarked_img_folder():
    watermarked_img_folder = os.path.join(os.path.dirname(__file__), 'watermarked_img')
    try:
        os.startfile(watermarked_img_folder)
    except Exception as e:
        messagebox.showerror("폴더 열기 오류", str(e))

# Tkinter GUI 설정
root = tk.Tk()
root.title("QR 코드 생성기")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# 서버 시작 버튼
start_server_btn = tk.Button(frame, text="서버 시작", command=start_server, width=30)
start_server_btn.grid(row=0, column=0, pady=5)

# QR 코드 생성 버튼
generate_qr_btn = tk.Button(frame, text="QR 코드 생성", command=generate_qr_codes, width=30)
generate_qr_btn.grid(row=1, column=0, pady=5)

# QR 코드 폴더 열기 버튼
open_qr_folder_btn = tk.Button(frame, text="QR 코드 폴더 열기", command=open_qr_folder, width=30)
open_qr_folder_btn.grid(row=2, column=0, pady=5)

# 원본 이미지 폴더 열기 버튼
open_origin_img_folder_btn = tk.Button(frame, text="원본 이미지 폴더 열기", command=open_origin_img_folder, width=30)
open_origin_img_folder_btn.grid(row=3, column=0, pady=5)

# QR 코드 추가된 이미지 폴더 열기 버튼
open_watermarked_img_folder_btn = tk.Button(frame, text="QR 코드 추가된 이미지 폴더 열기", command=open_watermarked_img_folder, width=30)
open_watermarked_img_folder_btn.grid(row=4, column=0, pady=5)

root.mainloop()
