#UPRAWNIENIA
#w - pisanie, tworzenie pliku
#r - czytanie
#a - apend (dołączać) = dopisywanie do pliku

plik = open("plik.txt", "a")

print(plik.writable())#czy można w nim pisać, czy jest otwarty z "w"

if plik.writable():
    plik.write(input("Podaj tekst: ") + "\n")#pisanie w pliku
plik.close()

plik = open("plik.txt", "r")

if plik.readable():
    print("ZAWARTOŚC PLIKU")
    tekst = plik.read()
    print(tekst)

plik.close()
plik = open("plik.txt", "r")

if plik.readable():
    print("ZAWARTOŚC Z TABLICY")
    tablica_z_tekstem = plik.readlines()#zczytuje linijka po linijce i dodale do tablicy
    for text in tablica_z_tekstem:
        print(text)

plik.close()
plik = open("plik.txt", "r")

if plik.readable():
    print("ZAWARTOŚĆ OD RAZU Z PLIKU")
    for l in plik:
        print(l)

plik.close()

plik = open("plik.txt", "w")

ile_bitow = plik.write(input("Podaj napis: "))#jesli damy do zmiannej to bedzie pokazywac ilosc bitow
print("Twoj wpis ma " + str(ile_bitow) + " bitow")