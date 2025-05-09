from flask import Flask, request
from PIL import Image
import os

app = Flask(__name__)

# 이미지를 저장할 경로 설정
upload_folder = '/Users/hyeonggeun_kim/Documents/22th_sw_contest/Object_Detection/collect_images'
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

@app.route('/upload', methods=['POST'])
def upload_file():
    """이미지를 수신하고 1280x800으로 변환하여 저장"""
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    # 파일 저장 경로 지정
    file_path = os.path.join(upload_folder, file.filename)
    
    # 이미지를 열고 해상도를 1280x800으로 변환
    try:
        img = Image.open(file)
        img_resized = img.resize((1280, 800))  # 해상도 변환
        img_resized.save(file_path)  # 변환된 이미지를 저장
    except Exception as e:
        return f'Error processing image: {str(e)}', 500
    
    return f'File {file.filename} uploaded and resized successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
