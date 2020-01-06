import requests
from bs4 import BeautifulSoup


def get_youtube_links(keyword):
    search_url = f'https://www.google.com/search?q={keyword}+site:youtube.com&tbm=vid'
    response = requests.get(search_url)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('a')
    youtube_video_url = 'youtube.com/watch'
    links = list(filter(lambda x: youtube_video_url in x['href'], links))

    youtube_links = set()
    for link in links:
        start_index = link['href'].index('https')
        end_index = link['href'].index('&sa=')
        # print(start_index, end_index)
        youtube_link = link['href'][start_index:end_index].replace('%3Fv%3D', '?v=')
        youtube_links.add(youtube_link)

    return youtube_links
