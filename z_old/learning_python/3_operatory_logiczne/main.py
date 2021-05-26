wiek = int(input("Podaj swój wiek: "))
gotowka = int(input("Podaj ilosc swojej gotowki: "))

#film +18 i 20zł za bilet
if wiek >= 18:
    if gotowka >= 20:
        print("#Mozesz wejsc do kina")

#zagnieżdżanie /\

# and = TRUE i TRUE -> TRUE  100% true       MA WYŻSZY PRIORYTET OD OR    jakby mnożenie
# or = TRUE i FALSE -> TRUE  jakaś prawda    Ma niższy priorytet od AND   jakby dodawawnie
# not = odwraca TRUE w FALSE i FALSE w TRUE

if wiek >= 18 and gotowka >= 20:
    print("Mozesz wejsc")
elif wiek < 18 or gotowka < 20:
    print("Nie mozesz wejsc do kina")
else:
    print("Błąd")

if not wiek >= 18:
    print("Dostajesz zniżkę na film dla dzieci!")

if True or False and False:
    #T + F * F
    #T or F and F
    #T + F
    #T or F
    #T
    print("True")
else:
    print("False")

# (True or False) and False
# (True) and False
# False