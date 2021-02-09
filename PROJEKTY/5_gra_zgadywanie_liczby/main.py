from random import randrange

print("Zagrajmy w grę: Zgadnij liczbę.")
print("Podaj zakres z jakiego mam wylosować liczbę!")

nmin = input("Podaj najmniejszą liczbę: ")
nmax = input("Podaj największą liczbę: ")

losowaLiczba = randrange(int(nmin),int(nmax)+1)# randrange(1,11) losuje wartość od 1 do 10

odpowiedz = -1
iloscOdpowiedzi = 0

print("Możemy zaczynać!")

while odpowiedz != losowaLiczba:
    iloscOdpowiedzi += 1
    odpowiedz = int(input("Podaj liczbę: "))
    if odpowiedz < losowaLiczba:
        print("Podałeś za małą liczbę!")
    elif odpowiedz > losowaLiczba:
        print("Podałeś za dużą liczbę!")

print("Brawo odgadłeś liczbę! Udało ci się to zrobić w ", str(iloscOdpowiedzi), " próbach!")