#tuple kolekcja krotka

lista = ["1", 2, "3"]
slownik = {1: "Jakub", "meferoanol": 3, 3: "angog"}


krotka = (2,4,8,16,32,64, "abcdefghijklmnoprst")

print(krotka[1])
print(krotka)

#nie można podmienić łatwo elementu w krotce
#krotka jest stałą

try:
    krotka[0] = 1
except:
    print("Błąd! Nie można podmieniać wartości in tuple!")

print(krotka.count(2))#ile razy występuje
print(krotka.index(2))#index tego obiektu




#wycinki, czyli części tablic, słowników, krotek

print(lista[1:4])#bierze obiekty od tego o indexie 1 do indexu 4 (BEZ 4 INDEXU)

try:
    print(slownik[1:2])
except:
    print("nie można wycinać słowników")

print(lista[1:10000])#mozna podać za dużo nie zwróci to błędu

print(lista[-3:-1])#można wycinać podając indexy od tyłu

print(krotka[0:7:2])#początek:koniec+1:co ile ma skakać

print(krotka[:3])#do 3
print(krotka[2:])#od 2

print(krotka[::-1])#wydrukuje od tyłu


