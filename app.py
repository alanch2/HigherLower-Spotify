from flask import Flask, redirect, url_for, render_template
import requests
import json
from data import spotify_token, playlist_id

app = Flask(__name__)


@app.route('/')
# landing page
def home():
    return render_template("index.html")


@app.route('/play')
# actual game page
def play():
    songs = []

    # get "Top 50 - USA" playlist data from spotify api
    query = "https://api.spotify.com/v1/playlists/{}".format(
            playlist_id)
    response = requests.get(query, headers={
                            "Content-Type": "application/json", "Authorization": "Bearer {}".format(spotify_token)})
    response_json = response.json()

    # iterate through data, putting name, artist(s), popularity, and cover image of each song into array
    playlist_data = response_json["tracks"]["items"]
    i = 1
    for item in playlist_data:
        track = item["track"]
        track_name = track["name"].replace("'", "")
        track_artist = []
        for artist in track["artists"]:
            track_artist.append(artist["name"])
        track_popularity = track["popularity"]
        track_img = track["album"]["images"][0]["url"]
        songs.append((track_name, track_artist, track_popularity, track_img))
        i += 1

    return render_template("play.html", songs=json.dumps(songs))


if __name__ == "__main__":
    app.run(debug=True)
