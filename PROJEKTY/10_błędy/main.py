#wyjątek to błąd

x = int(input())
y = int(input())

try:
    lista = []
    print(lista[0])
    print(x + "a")
    print(x / y)
except (ZeroDivisionError, TypeError):
    print("Wystąpił 1 z 2 błędów!")
except:
    print("Inne wyjątki!")
finally:#wykona się jak będzie błąd lub jak go nie bedzie
    print("To się wyświetli zawsze!")


print(x*y)



def dzielenie(x, y):
    assert y != 0, "Y==0"
    #wyświetli się ten kod błedu, tworzenie własnych błędów, pomaga przy sprawdzaniu kodu
    if y == 0:
        raise ZeroDivisionError("Nastąpiło dzielenie przez 0!")#wyrzucanie własnych wyjątków
    print(x/y)

try:
    dzielenie(1, 0)
except ZeroDivisionError:
    print("Błąd!")
    raise#wyświetli custom błąd, który może być dalej obsłużony



