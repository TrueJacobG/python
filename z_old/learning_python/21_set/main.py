# Zbiory -> Sets


liczby1 = {0, 4, 6, 8}

# Set, podobny do słownika

slowa = ["a", "b", "c", "d"]

slowa = set(slowa)

# Stworzenie setu z listy

print(liczby1)
print(slowa)

# wyświetla się zawsze w innej kolejności


liczby1.add(5)
print(liczby1)


liczby1.remove(5)
print(liczby1)


liczby1.add(0)
print(liczby1)
# nie dodaje tej samej wartości kolejny raz, właściwość zbioru -> set'u

test = [1, 1, 1, 1]
test = set(test)
print(test)
# w set'ie jest tylko 1


print(1 in liczby1)
# zwraca true lub false
# czy występuje ta wartość w zbiorze, działa na listach itd.


liczby2 = {2, 3, 8, 9}

print(liczby1 | liczby2)
# | == or
# wyświetla sumę zbiorów


print(liczby1 & liczby2)
# & == and
# wyświetla tylko część wspólną


print(liczby1 - liczby2)
# wyświetla zbiór 1 bez rzeczy ze zbioru 2
# odejmowanie


print(liczby1 ^ liczby2)
# wyświetlą się wszystkie bez tych co się powtórzą
# np. 8 występuje 2 razy wiec wyświetli się bez 8
# różnica symetryczna
