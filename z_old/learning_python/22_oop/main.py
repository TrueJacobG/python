# Programowanie obiektowe
# OOP

import numpy 

class Human:
    name = "Jakub"

    def __init__(self, wiek):
        # specjalna metoda, teraz tworząc obiekt trzeba podać tę zmienną
        self.wiek = wiek
        # tworzenie zmiennej globalnej

    def sayyourname(self, hello="Hello"):
        # self czyli z tej klasy, można zmienić self na inną nazwę
        return "{}, my name is ".format(hello) + self.name + " and I am " + str(self.wiek)


object1 = Human(24)
print(object1.name)
print(object1.sayyourname("Good morning"))

# tworzenie obiektu
# metody -> właściwości obiektu, funckjce obiektu

object1.name = "Gant"
print(object1.name)

# prosta zmiana KOPII właściwości w klasie

object2 = Human(18)
print(object2.name)

# inny obiekt dalej ma początkowe imię
