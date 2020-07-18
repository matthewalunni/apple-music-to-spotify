from bs4 import BeautifulSoup
from urllib import request
import requests

def getPlaylistJSON(url):
    htmlFile = request.urlopen(url)
    html = htmlFile.read()
    soup = BeautifulSoup(html, features="html.parser")
    songs = soup.find_all("div", {"class": "song-wrapper"})
    result = []
    for s in songs:
        song = "".join(s.find("div", {"class": "song-name"}).contents).strip()
        artist = "".join(s.find("a", {"class": "dt-link-to"}).contents).strip()
        entry = {
            "song": song,
            "artist": artist,
        }
        result.append(entry)
        pass
    return result

def getPlaylistName(url): 
    htmlFile = request.urlopen(url)
    html = htmlFile.read()
    soup = BeautifulSoup(html, features="html.parser")
    playlistName = soup.find("h1", {"class": "product-name typography-title-emphasized clamp-4"})
    return "".join(playlistName.contents).strip()

def returnTrack(songName, artist):
    endpoint_url = "https://api.spotify.com/v1/search?"
    o_auth = "BQDQw_-tZjiXtJE54YnTo7y11Y91tEl16x8Yt3h6k7W8-6RwbEfwqS50Joha1Hmh1lYMgDHwKIgNNS8UM4h26JdGbjJLjX42DH-l5XoI_O-puN32tZ7mAtfH7EwyBZM-UHkATZyDjTkDlQ0mhGDhnbIRo5eovbwQF7RZDavJAFAk-MWBuuJtoAocYqgCBaQ34AM"
    limit=30
    market="US"
    _type = "track"
    uris = [] 
    query = f'{endpoint_url}limit={limit}&market={market}&q={artist}&type={_type}'
    response =requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization": f"Bearer {o_auth}"})
    json_response = response.json()
    iterable_tracks = json_response["tracks"]['items']
    for i in iterable_tracks:
        if (i['name'].lower() == songName.lower()):
            if(i['artists'][0]["name"].lower() == artist.lower()):
                uris.append(i)
                print(f"\"{i['name']}\" by {i['artists'][0]['name']}")
            pass
    pass

if __name__ == "__main__":
    
    print("Enter the URL of the apple music playlist you wish to convert: ")
    URL = "https://music.apple.com/ca/playlist/groovy-bangers/pl.u-KVXBBPJtmmprRR"
    # URL = input().strip()
    print("The URL we will convert is " + URL)    
    print("Playlist Name: " + getPlaylistName(URL))
    for entry in getPlaylistJSON(URL):
        try:
            # print("Song: " + entry["song"] + ", Artist: " + entry["artist"])
            returnTrack(entry["song"], entry["artist"])
            pass
        except:
            pass
        pass
    pass

