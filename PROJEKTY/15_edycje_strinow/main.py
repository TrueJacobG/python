lista = ["a", "b", "c"]

print(", ".join(lista))#1 string wstawiany jest pomiędzy dane elementy listy

print("Witaj Święty Mikołaju!".replace("Witaj", "Cześć"))#znajduje 1 ciąg i zamienia na 2

print("To zdanie.".startswith("To"))#zwraca true albo false jeśli string zaczyna się od danego słowa

print("To zdanie.".endswith("."))#czy kończy się na dany znak

print("i" in "To zdanie.")#czy jest ten znak

print("To zdanie.".upper())#duże litery

print("To zdanie.".lower())#małe litery

lista1 = [1,2,5,7,10,24,70]

if all([int(i)>0 for i in lista1]):#all sprawdza dla każdego elementu listy czy spełnia warunek
    print("Wszystkie liczby są większe od 0")
else:
    print("Wszystkie liczby nie są większe od 0")

if any([i % 2 == 0 for i in lista1]):#jeśli jaki kolwiek spełnia warunek
    print("Jakaś liczba w tej liście jest parzysta")


for i in enumerate(lista1):#ponumerowanie wartości w liście
    print(i[0]+1, "-", i[1])#tworzone są tuple (nr , wartość)


