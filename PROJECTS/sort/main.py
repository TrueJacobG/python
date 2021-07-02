# Sortowanie alfabetycznie
# .sort działa tylko na listach

lista = ['Jabłka', 'Marchewki', 'Brzoskwinie',
         'Gruszlo', 'Kalafiory', 'Żotkiew']

lista1 = [1, 2, 3, 4, 5]

lista.sort(reverse=True)
# od tyłu
lista1.sort()

print(lista)
print(lista1)


# .sorted działa też na słownikach

dictionary = {2: "Jabłka", 7: 'Marchewki', 10: 'Brzoskwinie'}

x = dict(sorted(dictionary.items(), key=lambda item: item[1]))
# funkcja anonimowa, a oznacza def item(item)
#                               return item[1]
# czyli zwraca 2 element
print(x)
