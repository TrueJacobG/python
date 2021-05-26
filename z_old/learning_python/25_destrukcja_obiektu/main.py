# Klasy - destruktor
# Cykl życia

class Test:
    #def __new__(cls):
        #print("Hello class!")
    # podczas tworzenia obeiktu
    # NIE UŻYWAĆ NARAZIE, NIEBEZPIECZNE, łATWO POPSUĆ PLIK

    def __del__(self):
        # kiedy niszczymy obiekt, kiedy program kończy się wykonywać to niszczone są wszystkie obiekty
        print("Bye class!")


obiekt1 = Test()

print("KONIEC")
# __del__ wykonuje się na końcu programu, więc po ostatniej linijce kodu

obiekt2 = Test()
del obiekt2
# również wywoła się __del__

obiekt3 = Test()
obiekt4 = obiekt3
del obiekt3
# teraz metoda __del__ nie zadziała bo dalej istnieje obiekt4 w klasie Test()
# jeśli jest jakaś referencja do klasy to del "obiekt" nie zadziała

obiekt5 = Test()
lista = [obiekt5]
del obiekt5
# również nie zadziała del bo dalej obiekt jest na liście; referencja
