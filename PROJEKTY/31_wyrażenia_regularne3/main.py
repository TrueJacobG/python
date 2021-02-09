import re

if re.match("[A-Z][a-z]", "Afa"):
    print("Dopasowano")
else:
    print("Nie dopasowano")
# metoda match sprawdza tylko początek dlatego może być więcej niż 2 znaki,
# jak tam $ na koniec to będzie można tylko 2 znaki

if re.match("^[A-Za-z]*$", "asldijfbpdisufgbp"):
    print("Dopasowano")
else:
    print("Nie dopasowano")
# * pozwala na powtarzanie określonego zbioru lub znaku dowolną ilość razy, również 0
# + działa podobnie ale musi być min. 1 raz

if re.match("^[A-Za-z]?[a-z]$", "az"):
    print("Dopasowano")
else:
    print("Nie dopasowano")
# ? znak może pojawić się 1 raz lub 0
# brak znaku znaczy, że musi się 1 raz pojawić

if re.match("^[A-Za-z]{3,6}$", "azgg"):
    print("Dopasowano")
else:
    print("Nie dopasowano")
# znak musi powtórzyć się min 3razy max 6razy
# można nie podawać górnego limitu
# można nie podawać dolnego limitu


