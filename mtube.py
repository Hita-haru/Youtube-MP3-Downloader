import yt_dlp
import ffmpeg
import os

def download_and_convert_to_mp3(video_url, output_path):
    # ダウンロード設定
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'ffmpeg_location': 'C:/ffmpeg/bin'  # ffmpegのパスを指定
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# ユーザーから入力を取得
video_url = input("YouTubeの動画URLを入力してください: ")
output_path = input("出力ディレクトリのパスを入力してください: ")

download_and_convert_to_mp3(video_url, output_path)
