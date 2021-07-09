# scrapes Spotify's Top200 Charts Page
import requests
from bs4 import BeautifulSoup

HOME_URL = "https://spotifycharts.com/regional/global/daily/latest"
HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

response = requests.get(HOME_URL, headers=HEADERS)

if response.status_code == 200:
    print('Success!')
else:
    print('Fail :(')

soup = BeautifulSoup(response.content.decode('utf-8'), "html.parser")
print(soup.prettify())
