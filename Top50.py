from selenium import webdriver
from Scroller import scroll

URL = "https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp"
PATH = 'M:\Programming\Python Support Files\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(PATH)

class Song:
    def __init__(self, rank, title, artist, plays, album, playtime):
        self.rank = rank
        self.title = title
        self.artist = artist
        self.plays = plays
        self.album = album
        self.playtime = playtime


top50 = []


