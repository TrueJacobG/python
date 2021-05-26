# Metody magiczne

import math as matematyka  # nietypowa nazwa biblioteki


class Punkt2d:
    def __init__(self, x, y):
        # gdy tworzymy klasę to się wywołuje
        self.x = x
        self.y = y
        self.odleglosc = matematyka.sqrt(x**2 + y**2)
        # math.sqrt -> pierwiastek

    def __add__(self, drugi):
        # kiedy chcesz dodać do siebie obiekty tej klasy to co ma się zadziać
        return Punkt2d(self.x + drugi.x, self.y + drugi.y)
        #               /\                   /\
        # te dane które zostały podane przy tworzeniu pierwszego obiektu
        #
        # drugi.x i drugi.y -> dane podane przy stworzeniu drugiego obiektu

    def __sub__(self, drugi):
        # kiedy chcesz odjąć to co ma się zdarzyć
        return Punkt2d(self.x - drugi.x, self.y - drugi.y)

    # inne funkcje magiczne dotyczące działań to np. :
    # __mul_ = mnożenie
    # __div__ = dzielenie

    def __lt__(self, drugi):
        # less than = mniejsze niż
        return self.odleglosc < drugi.odleglosc
        # zwraca true (jeśli jest mniejsza) lub false (jeśli jest większa)

    def __eq__(self, drugi):
        if self.x == drugi.x and self.y == drugi.y:
            return "tak są równe"
        return "nie są równe"

    # inne funkcje magiczne porównań to np. :
    # __ge__ = greater equal = wieksze równe
    # __gt__ = greater than = większy od
    # __le__ = less equal = mniejszy równy
    # __ne__ = not equal = negacja równy -> !=
    # __eq__ = równy

    def __len__(self):
        return int(round(self.odleglosc, 0))
        # zaokrąglanie odległości


p1 = Punkt2d(2, 5)
p2 = Punkt2d(4, 6)
p3 = p1 + p2
# Dodawanie do siebie obiektów <- __add__
print(p3.x)
print(p3.y)

p4 = p1 - p2
# Odejmowanie od siebie obiektów <- __sub__
print(p4.x)
print(p4.y)

print(p1.odleglosc)
print(p2.odleglosc)
print(p1 < p2)
print(p1 > p2)

print(p1 == p1)
# porównuje ze sobą 2 wartości więc odpala się metoda __eq__
print(p1 == p2)

print(p1.odleglosc)
print(len(p1))
# zadeklarowałeś funkcje magiczną __len__ więc teraz jak chcesz przybliżyć to dzieje się to co zadeklarowałeś
