# Regular Expressions

import re

if re.match("\?", "kot"):
    print("Znalazłem!")
else:
    print("Nie znalazłem!")

# opcje klucza:
# . -> dowolna litera, liczba lub znak
if re.match("ko.", "kot"):
    print("Znalazłem!")
else:
    print("Nie znalazłem!")
# ^ -> MUSI zaczynać się w taki sposób
# $ -> musi się kończyć w tym miejscu, musi być tyle znaków
if re.match("^ko.$", "kotyyyyy"):
    # muszą być 3 litery, dwie pierwsze to "K""O", a trzecia dowolna
    print("Znalazłem!")
else:
    print("Nie znalazłem!")
# [Oo] -> klasa znaków, zbiór znaków; ta litera musi być z tego zbioru
if re.match("[kK]ot", "kot"):
    print("Znalazłem!")
else:
    print("Nie znalazłem!")
# [A-Z] -> z tablicy ascii znaki od A do Z
# [a-z] -> od a do z
# [a-zA-Z] -> wszystkie litery bez polskich znaków
if re.match("[a-z]o.", "kot"):
    print("Znalazłem!")
else:
    print("Nie znalazłem!")
# [^A-Z] -> nie może w tym miejscu wystąpić duża litera

