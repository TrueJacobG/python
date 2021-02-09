#Sprawdzanie czyt imię jest męskie czy żeńskie

#name = input("Podaj swoje imię: ")

#if name[-1] != "a":#ostatni znak
#    print("Propably you're a man")
#else:
#    print("Propably you're a woman")

import random

randomowa = str(random.randrange(1,11))

plik = open("numer.txt", "a")

if plik.writable():
    plik.write(randomowa + "\n")
else:
    print("Nie można tego zrobić!")

plik.close()

plik = open("numer.txt", "r")

if plik.readable():
    print(plik.read())
else:
    print("Nie można odczytać danych z pliku!")