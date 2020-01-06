import glob

from pytube import YouTube


def download_videos(youtube_links):
    for youtube_link in youtube_links:
        local_videos = glob.glob('*.mp4')
        videos_count = len(local_videos)
        if videos_count < 3:
            download_video(youtube_link)
        else:
            print(f'Already download three videos: {local_videos}')
            break


def download_video(link):
    try:
        yt = YouTube(link)
        print(f'Download: {yt.title}')

        yt.streams \
            .filter(only_audio=True) \
            .first() \
            .download()

    except KeyError:
        print(f"can't download this video: {link}")
