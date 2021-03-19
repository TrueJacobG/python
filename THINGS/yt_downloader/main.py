from pytube import YouTube

url = input("Podaj link do filmu który chcesz pobrać: ")

choice = input(
    "Co chcesz zrobić?\n 1. Pobrać tylko audio 2. Pobrać cały film\n")

try:
    if int(choice) == 1:
        ytd = YouTube(url).streams.filter(only_audio=True).filter(
            file_extension='mp3').first().download()
    else:
        ytd = YouTube(url).streams.first().download()

    slash = ytd.rfind("\\")+1
    print('\033[92m' + ytd[slash:] +
          " DOWNLOADED SUCCESSFULLY" + '\033[0m')
except:
    print('\033[91m' + "SOMETHING IS WRONG!" + '\033[0m')
