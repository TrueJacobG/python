from pytube import YouTube
from moviepy.editor import *
from os import remove

url = input("Podaj link do filmu który chcesz pobrać: ")

choice = input(
    "Co chcesz zrobić?\n 1. Pobrać tylko audio 2. Pobrać cały film\n")
try:
    if int(choice) == 1:
        ytd = YouTube(url).streams.filter(
            file_extension='mp4').first().download()
        slash = ytd.rfind("\\")+1

        mp4 = f"{ytd[slash:]}"
        mp3 = mp4.replace(".mp4", ".mp3")

        videoClip = VideoFileClip(mp4)
        audioclip = videoClip.audio

        audioclip.write_audiofile(mp3)
        audioclip.close()
        videoClip.close()
        remove(mp4)
    else:
        ytd = YouTube(url).streams.first().download()
        slash = ytd.rfind("\\")+1

    print('\033[92m' + ytd[slash:] + " DOWNLOADED SUCCESSFULLY" + '\033[0m')
except:
    print('\033[91m' + "SOMETHING IS WRONG!" + '\033[0m')
