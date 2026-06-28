import requests, os, json
from dotenv import load_dotenv

load_dotenv()

LAST_FM_USERNAME = os.getenv("LAST_FM_USERNAME")
API_KEY = os.getenv("API_KEY")
APPLICATION_ID = os.getenv("APPLICATION_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")

def getUserInfo():
    getUserData = requests.get(url=f"http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user={LAST_FM_USERNAME}&api_key={API_KEY}&format=json")
    userData = getUserData.json()

    scrobbles = int(userData["user"]["playcount"])
    totalArtists = int(userData["user"]["artist_count"])

    return scrobbles, totalArtists

def getWeeklyInfo(period= "7day", limit= 1):
    getWeeklyTrack = requests.get(url=f"http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={LAST_FM_USERNAME}&period={period}&limit={limit}&api_key={API_KEY}&format=json")
    getWeeklyAlbum = requests.get(url=f"http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user={LAST_FM_USERNAME}&period={period}&limit={limit}&api_key={API_KEY}&format=json")
    getWeeklyArtist = requests.get(url=f"http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={LAST_FM_USERNAME}&period={period}&limit={limit}&api_key={API_KEY}&format=json")

    trackData = getWeeklyTrack.json()
    albumData = getWeeklyAlbum.json()
    artistData = getWeeklyArtist.json()

    track = f"{trackData["toptracks"]["track"][0]["artist"]["name"]} - {trackData["toptracks"]["track"][0]["name"]}"
    album = f"{albumData["topalbums"]["album"][0]["artist"]["name"]} - {albumData["topalbums"]["album"][0]["name"]}"
    artist = f"{artistData["topartists"]["artist"][0]["name"]} - {artistData["topartists"]["artist"][0]["playcount"]} scrobbles"

    return track, album, artist

def getRecentScrobble(limit= 1):
    getScrobble = requests.get(url=f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={LAST_FM_USERNAME}&limit={limit}&api_key={API_KEY}&format=json")
    scrobbleData = getScrobble.json()

    latestScrobble = f"{scrobbleData["recenttracks"]["track"][0]["artist"]["#text"]} - {scrobbleData["recenttracks"]["track"][0]["name"]}"

    return latestScrobble

def update():
    scrobbles, totalArtists = getUserInfo()
    track, album, artist = getWeeklyInfo()
    recentScrobble = getRecentScrobble()

    jsonString = {"data":{"dynamic":[{"type":2,"name":"scrobbles","value":scrobbles},{"type":1,"name":"latestscrobble","value":f"{recentScrobble}"},{"type":2,"name":"artistscrobbled","value":totalArtists},{"type":1,"name":"topartist","value":artist},{"type":1,"name":"topalbum","value":album},{"type":1,"name":"topsong","value":track}]}}

    r = requests.patch(url=f"https://discord.com/api/v9/applications/{APPLICATION_ID}/users/{USER_ID}/identities/0/profile", headers={"Content-Type": "application/json", "Authorization": f"Bot {BOT_TOKEN}", "User-Agent": "DiscordBot (https://github.com/discord/discord-api-docs, 1.0.0)"}, data=json.dumps(jsonString))
    print(r)


update()