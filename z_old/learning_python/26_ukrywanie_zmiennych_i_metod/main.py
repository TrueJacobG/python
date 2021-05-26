# Klasy ukrywanie danych


class Test:
    lista = []

    def dodaj(self, arg):
        self.lista.append(arg)
        # dodawanie nowego atgumentu do listy

    def zdejmij(self):
        if len(self.lista) > 0:
            return self.lista.pop(len(self.lista) - 1)
            # usuwanie ostatniego argumentu z listy
        else:
            return


class Test2:
    _lista = []
    # PRYWATNA ZMIENNA, można też tak ukrywać metody
    # robi się to bo to by metodami publicznymi korzystać z klasy

    __lista1 = []
    # super prywatna lista, jeszcze trudniejsza do dostania się

    def dodaj(self, arg):
        return self._lista.append(arg)

    def zdejmij(self):
        if len(self._lista) > 0:
            return self._lista.pop(len(self._lista) - 1)
        else:
            return


obj = Test()

obj.dodaj("A")
obj.dodaj("B")
print(obj.lista)
# dodawanie i wyświetlanie listy z klasy

obj.zdejmij()
# usuwanie ostatniego

obj.lista.append("C")
# lista nie jest ukryta więc można do niej w prosty sposób coś dodać

print(obj.lista)

# ###################################


obj2 = Test2()

obj2.dodaj("1")
obj2.dodaj("2")

print(obj2._lista)
# wyświetla się błąd bo jest to tylko informacja dla użytkownika
# i mimo wszystko dalej może skorzystać z tej tablicy

obj2._lista.append("3")
print(obj2._lista)
# dodaje ale wyświetla się błąd soft

obj2._Test2__lista1.append("Niestety dalej można dostać się do super prywatnej tablicy")
print(obj2._Test2__lista1)
# do super tajnej tablicy dalej można się dostać dzięki podaniu _ nazwa klasy i __
