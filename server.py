from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Google Sheets NoCodeAPI URL
SHEET_API_URL = "https://v1.nocodeapi.com/roy995700/google_sheets/qkULgqNPMqHHZkNt?tabId=sheet1"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # ফাইল সার্ভারে সেভ করব না

    # ধরুন ফাইলের URL এমনভাবে তৈরি হবে (আপনি নিজের ক্লাউড বা CDN এর URL দিতে পারেন)
    # এখন শুধু ফাইল নাম ধরে URL বানাচ্ছি ধরুন
    file_url = f"https://yourcdn.com/uploads/{file.filename}"

    # Google Sheets-এ আপলোডের জন্য রো তৈরি করছি
    sheet_row = [[file.filename, file_url]]

    # Google Sheets API POST
    response = requests.post(SHEET_API_URL, json=sheet_row)

    if response.status_code == 200:
        return jsonify({
            'message': 'File info uploaded to Google Sheets successfully!',
            'file_name': file.filename,
            'file_url': file_url
        })
    else:
        return jsonify({
            'error': 'Failed to save data to Google Sheets',
            'details': response.text
        }), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
