from bs4 import BeautifulSoup
from urllib import request
import re


print("Enter the URL of the apple music playlist you wish to convert: ")
URL = "https://music.apple.com/ca/playlist/groovy-bangers/pl.u-KVXBBPJtmmprRR"

print("The URL we will convert is " + URL)

htmlFile = request.urlopen(URL)
html = htmlFile.read()

soup = BeautifulSoup(html, features="html.parser")

songs = soup.findAll("span", {"class": "tracklist-item__text__headline"})
artists = soup.findAll("a", {"class": "table__row__link table__row__link--secondary"})
count = 0
for i in range(len(songs)):
    currentSong = songs[i].text.rstrip()
    currentArtist = artists[i].text.rstrip()
    print(currentSong + ', ' + currentArtist)
