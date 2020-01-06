"""
python 輸入「keyword」
抓取 youtube 來源 3 個影片的聲音存檔
檔名為影片標題
"""
from .args_helper import get_keyword
from .google_search_crawler import get_youtube_links
from .pytube_helper import download_videos

keyword = get_keyword()
print(f'Keyword: {keyword}')

youtube_links = get_youtube_links(keyword)
print(youtube_links)

download_videos(youtube_links)
print('Finished!')
