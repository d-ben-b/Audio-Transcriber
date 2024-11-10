import torch
def download_audio(url):
    import yt_dlp

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'geo_bypass': True,
        'nocheckcertificate': True,
        'outtmpl': 'downloaded_audio.%(ext)s',  # 指定輸出文件名
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # 可調整音質，數值越高音質越高
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title')
            print(f"音訊 '{title}' 已成功下載並轉換為 MP3 格式！")
    except Exception as e:
        print(f"下載失敗: {e}")
        return


print("Using GPU" if torch.cuda.is_available() else "Using CPU")
