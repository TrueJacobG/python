lista = [1, 4, 6, 8, 9, 10]


def funkcja(x):
    return x * 3


# Mapy
# służą do modyfikacji kolekcji


wynik = map(funkcja, lista)
# funkcja map przyjmuje funkcje i kolekcje np. liste,
# wykonuje te funkcje na każdym elemencie z kolekcji, iteracja

print(list(wynik))

wynik2 = map(lambda x: x * x, lista)
# mapa na funkcji anonimowej

print(list(wynik2))

# Filtry
# służą do odfiltrowywania rzeczy z listy

wynik3 = filter(lambda x: x % 2 == 0, lista)

# wyświetli tylko te liczby które spełnią warunek czyt. dadzą true

print(list(wynik3))
