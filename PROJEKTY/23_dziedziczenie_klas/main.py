# Dziedziczenie klas

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    # dziedziczenie klas
    # odziedziczanie właściwości po rodzicu; drzewo genealogiczne
    def voice(self):
        return "HOW HOW :D"


class Wolf(Dog):
    def introduce(self):
        return "I am a Wolf and I am doing " + super().voice()
        # super to taki self -> szuka funckji/metody w klasie rodzicu


class Cat(Animal):
    def voice(self):
        return "Meow meow"


dog = Dog("Rex", 5)
print(dog.voice())

cat = Cat("Misio", 3)
print(cat.voice())

wolf = Wolf("Mareczek", 4)
print(wolf.introduce())


