from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import tempfile
import subprocess
import uuid

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '✅ WhisTube API 正常啟動，請以 POST 呼叫 /api/whistube'

@app.route('/api/whistube', methods=['POST'])
def whistube():
    data = request.get_json()
    yt_url = data.get('yt_url')

    if not yt_url:
        return jsonify({'success': False, 'message': '缺少 yt_url'}), 400

    try:
        uid = str(uuid.uuid4())[:8]
        temp_dir = tempfile.mkdtemp()

        audio_path = os.path.join(temp_dir, f"{uid}.wav")
        srt_path = os.path.join(temp_dir, f"{uid}.srt")
        txt_path = os.path.join(temp_dir, f"{uid}.txt")

        subprocess.run([
            "yt-dlp", "-x", "--audio-format", "wav",
            "-o", audio_path, yt_url
        ], check=True)

        subprocess.run([
            "whisper", audio_path, "--model", "base", "--output_format", "srt", "--output_dir", temp_dir
        ], check=True)

        subprocess.run([
            "whisper", audio_path, "--model", "base", "--output_format", "txt", "--output_dir", temp_dir
        ], check=True)

        public_dir = os.path.join("static", uid)
        os.makedirs(public_dir, exist_ok=True)

        os.rename(os.path.join(temp_dir, f"{uid}.srt"), os.path.join(public_dir, "output.srt"))
        os.rename(os.path.join(temp_dir, f"{uid}.txt"), os.path.join(public_dir, "output.txt"))

        return jsonify({
            'success': True,
            'srt_url': f"/static/{uid}/output.srt",
            'txt_url': f"/static/{uid}/output.txt"
        })

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
