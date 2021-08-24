import requests
import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
from search import *
import random

# Constants
base = "https://api.genius.com"
client_access_token = "-q1tRGBZMEOk6JewZCC_KWZBxyFSg9nccGlX11Cb3MxpGpzWG4FBSJIXCJS33D3x"


def connect_lyrics(song_id):
    # Constructs the path of song lyrics
    url = "songs/{}".format(song_id)
    data = get_json(url)

    # Gets the path of song lyrics
    path = data['response']['song']['path']

    return path


def retrieve_lyrics(song_id):
    # Retrieves lyrics from html page
    path = connect_lyrics(song_id)

    URL = "http://genius.com" + path
    page = requests.get(URL)

    # Extract the page's HTML as a string
    html = BeautifulSoup(page.text, "html.parser")

    # Scrape the song lyrics from the HTML
    try:
        lyrics = html.find("div", class_="lyrics").get_text()
        return lyrics
    except:
        return None


def get_song_id(artist_id):
    # Get all the song id from an artist
    current_page = 1
    next_page = True
    songs = []  # to store final song ids

    while next_page:
        path = "artists/{}/songs/".format(artist_id)
        params = {'page': current_page}  # the current page
        data = get_json(path=path, params=params)  # get json of songs

        page_songs = data['response']['songs']
        if page_songs:
            # Add all the songs of current page
            songs += page_songs
            # Increment current_page value for next loop
            current_page += 1
            print("Page {} finished scraping".format(current_page))
            # LIMITER
            # TODO:
            if current_page == 5:
                next_page = False
                break

        else:
            # If page_songs is empty, quit
            next_page = False

    print("Song id were scraped from {} pages".format(current_page))

    # Get all the song ids, excluding not-primary-artist songs.
    songs = [song["id"] for song in songs
             if song["primary_artist"]["id"] == artist_id]

    return songs


def get_song_information(song_ids):
    # Retrieve meta data about a song
    # initialize a dictionary.
    song_list = {}
    #print("Scraping song information")
    for i, song_id in enumerate(song_ids):
        #print("id:" + str(song_id) + " start. ->")
        path = "songs/{}".format(song_id)
        data = get_json(path=path)["response"]["song"]

        song_list.update({
            i: {
                "title": data["title"],
                "release_date": data["release_date"] if data["release_date"] else "unidentified",
                "producer_artists":
                [feat["name"] if data["producer_artists"]
                    else "" for feat in data["producer_artists"]],
                "writer_artists":
                [feat["name"] if data["writer_artists"]
                    else "" for feat in data["writer_artists"]],
                "genius_track_id": song_id,
            }
        })

        #print("-> id:" + str(song_id) + " is finished. \n")
    return song_list


def getArtistId():
    while True:
        name = input("Podaj artyste, ktorego piosenke chcesz zgadąć: ")
        name = name.encode("ascii", "ignore")
        name = name.decode()
        name = name.capitalize().replace(" ", "-")
        url = "https://genius.com/artists/" + name
        website = requests.get(url)
        if "Burrr!" in website.text:
            print("Podałeś złą nazwę artysty. Spróbuj jeszcze raz!")
            continue
        site = website.text
        site = site.encode("ascii", "ignore")
        site = site.decode()
        location = site.find("songs?for_artist_page=")+22
        artist_id = ""
        while True:
            try:
                idNumber = int(site[location])
                artist_id += str(idNumber)
                location += 1
            except:
                break
        break
    return int(artist_id)


def main(artist_id, songs_ids, length):
    randomNumber = random.randint(0, length-2)
    songs_ids = songs_ids[randomNumber:randomNumber+1]

    # Scrape lyrics from the songs
    song_lyrics = [retrieve_lyrics(song_id) for song_id in songs_ids]

    for lyrics in song_lyrics:
        if lyrics == None:
            return
        print(lyrics)

    # Get meta information about songs
    song_list = get_song_information(songs_ids)
    print(song_list)

    wait = input()

    # Shows some random songs from arist and lyrics
    # search(term)


if __name__ == "__main__":
    artist_id = getArtistId()
    songs_ids = get_song_id(artist_id)
    length = len(songs_ids)
    while True:
        main(artist_id, songs_ids, length)
