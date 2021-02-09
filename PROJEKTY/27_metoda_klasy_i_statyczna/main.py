# Metody klas i statyczne

class Human:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw_sie(self):
        print("Mam na imię " + self.imie)

    @classmethod
    # dzięki temu można teraz wywołać klasę po tej metodzie
    def nowy_czlowiek(cls, imie):
        return cls(imie)

    @staticmethod
    # bardzo podobna ale nie przyjmuje argumentu "cls", czyli takiego trochę self
    def przywitaj_sie(arg):
        print("Siema " + arg)



cz1 = Human.nowy_czlowiek("Cezary Baryka")
# nie trzeba tworzyć obiektu bo można wykorzystać metodę od razu

cz1.przedstaw_sie()
# odwołuję się teraz do całej klasy i jestem tam imię

cz2 = Human("ZiomsonPL")
cz2.przedstaw_sie()
# dalej można stworzyć obiekt i skorzystać z tej klasy obiektowo

Human.przywitaj_sie("Jakub")
# bez tworzenia obiektu
