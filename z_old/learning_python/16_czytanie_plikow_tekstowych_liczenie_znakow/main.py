plik = open("text.txt", "r")

tekst = plik.read()

plik.close()


def policz(txt, znak):
    licznik = 0
    for litera in txt:
        if znak == litera:
            licznik += 1
    return licznik

print(policz(tekst.lower(), "a"))#liczy ile razy wystąpił ten znak w tekście, nie ważny czy duży znak czy mały

calosc = 0

for z in "abxdefghijklmnoprstwuyz":
    ile = policz(tekst.lower(), z)
    procent = 100 * ile / len(tekst)#jaki procent całości tekstu stanowi każda litera
    print("{0} - {1} - {2}%".format(z.upper(), ile, round(procent)))#zaokrąglanie
    calosc = procent + calosc

print(round(calosc),"%")#jaką część całego tekstu stanowi suma wszystkich liter alfabetu


#alt + j -> dodaj do zaznaczenia
#ctrl + f -> szukanie w tekście