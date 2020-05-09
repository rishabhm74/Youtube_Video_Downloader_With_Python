import youtube_dl

ydl_opts = {}

def dwl_vid():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([zxt])

channel = "y"

while(channel == "y" or channel == "Y"):
    link_of_video = input("Enter video URL:")
    zxt = link_of_video.strip()

    dwl_vid()
    channel = input("Do you want to download another video? [y/n]")