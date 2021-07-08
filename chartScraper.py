# scrapes Spotify's Top200 Charts Page
import requests
from bs4 import BeautifulSoup

HOME_URL = "https://spotifycharts.com/regional/global/daily/latest"
