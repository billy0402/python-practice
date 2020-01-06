import requests
from bs4 import BeautifulSoup


def get_youtube_links(keyword):
    base_url = 'https://www.youtube.com'
    search_url = f'{base_url}/results?search_query={keyword}'
    response = requests.get(search_url)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('a.yt-uix-tile-link')

    youtube_links = set()
    for link in links:
        youtube_link = base_url + link['href']
        youtube_links.add(youtube_link)

    return youtube_links
