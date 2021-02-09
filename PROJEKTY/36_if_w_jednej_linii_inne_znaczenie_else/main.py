# Skrócony operator if

print("Prawda") if 2 > 1 else print("Nieprawda")
# skrócony if

zmienna = "Zimsonpl" if 10 % 3 == 0 else "Nie ziomsonpl"

print(zmienna)


# Inne wykorzystanie słowa else

for x in range(10):
    if x > 3:
        break
else:
    print("Koniec")
# kiedy pętla kończy się break'iem to nie wyświetli się else, ale jeśli nie to wyświetli się po pętli


try:
    b = 1/0
except ZeroDivisionError:
    print("Nie wolno dzielić przez zero!")
else:
    print("ZZA")
# jeśli nie wystąpi błąd to wyświetli else
finally:
    print("Wyświetlam się zawsze!")
