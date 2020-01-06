import glob
import json
import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from pytube import YouTube


def download_videos(youtube_links):
    videos_infos = []

    for youtube_link in youtube_links:
        local_videos = glob.glob('*.mp4')
        videos_count = len(local_videos)

        if videos_count < 10:
            download_video(youtube_link)
            videos_info = get_video_info(youtube_link)
            videos_infos.append(videos_info)
        else:
            print(f'Already download ten videos: {local_videos}')
            break

    videos_infos_to_json(videos_infos)


def download_video(link):
    try:
        yt = YouTube(link)
        print(f'Download: {yt.title}')

        yt.streams \
            .first() \
            .download()

    except KeyError:
        print(f"can't download this video: {link}")


def get_video_info(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    filename = soup.select_one('span.watch-title').text.strip()
    watches_text = soup.select_one('div.watch-view-count').text.strip()
    watches = re.search("觀看次數：(.*)次", watches_text).group(1)
    likes = soup.select_one('button.like-button-renderer-like-button span').text.strip()
    dislikes = soup.select_one('button.like-button-renderer-dislike-button span').text.strip()
    date_text = soup.select_one('div#watch-uploader-info').text.strip()
    date = re.search("發布日期：(.*)", date_text).group(1)

    return {"filename": filename, "url": link, "watches": watches, "likes": likes, "dislike": dislikes, "date": date}


def videos_infos_to_json(infos):
    today_text = datetime.now().strftime("%Y%m%d")
    with open(f'{today_text}-youtube.json', 'w+', encoding='UTF-8') as file:
        json.dump(infos, file, ensure_ascii=False)
