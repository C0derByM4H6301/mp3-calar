import youtube_dl

options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}


url = 'https://www.youtube.com/watch?v=Vu1pOXXGIso'

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([url])
