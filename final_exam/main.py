"""
程式主要功能為透過 youtube 搜尋(亦可透過 google，但限搜尋 youtube 影片)並抓取影片，且透過 json 檔儲存相關資訊
1. 程式需詢問使用者要搜尋的關鍵字
2. 抓取 youtube 搜尋結果的前十個影片，並依標題名稱存成檔案(格式不拘，需為影片)
3. 用 json 檔案記錄該影片的資訊，檔名為今日日期(yyyyMMdd-youtube.json)，內容應為
"""
from .youtube_download_helper import download_videos
from .youtube_search_crawler import get_youtube_links

keyword = input('請輸入你想搜尋的影片關鍵字: ')
print(f'Keyword: {keyword}')

youtube_links = get_youtube_links(keyword)
print(f"共有 {len(youtube_links)} 個影片連結", youtube_links)

download_videos(youtube_links)
print('Finished!')
