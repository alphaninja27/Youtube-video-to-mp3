import youtube_dl


def get_mp3():
    vid_info = youtube_dl.YoutubeDL().extract_info(
        url = input("Enter video URL: "), download = False
    )

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': f"{vid_info['title']}.mp3",
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([vid_info['webpage_url']])
