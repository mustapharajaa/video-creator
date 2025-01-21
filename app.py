from flask import Flask, request, send_file
from moviepy.editor import ImageClip, AudioFileClip
import os

app = Flask(__name__)

@app.route('/create_video', methods=['POST'])
def create_video():
    # تحميل الصورة والصوت من الطلب
    image = request.files['image']
    audio = request.files['audio']

    # حفظ الملفات مؤقتًا
    image_path = "temp_image.jpg"
    audio_path = "temp_audio.mp3"
    output_video_path = "output_video.mp4"

    image.save(image_path)
    audio.save(audio_path)

    # إنشاء الفيديو
    image_clip = ImageClip(image_path)
    audio_clip = AudioFileClip(audio_path)
    image_clip = image_clip.set_duration(audio_clip.duration)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.write_videofile(output_video_path, fps=24)

    # إرسال الفيديو كاستجابة
    return send_file(output_video_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
