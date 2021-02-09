#WYRAŻENIA LISTOWE

lista = list(range(1,11))#list -> zamiana w liste, range->liczby do 'x' bez 'x' do 'y'

print(lista)

nowa = [i * 2 for i in lista]
#dla każdej wartości z listy stwórz wartość w nowej liście *2   'i' nowa wartość

print("Nowa",nowa)

nowa2 = [i+2 for i in lista if i % 2 == 0]#tylko liczby parzyste z 1 listy zostaną wybrane
#i to każda rzecz po kolei z listy która jest sprawdzana if'em i jeśli spełnia warunek
#to zapisana jest w nowej liście jako {wzór}, czyli w tym wypadku i+2

print("Nowa2", nowa2)



#FORMATOWANIE STRING'ÓW

argument = ["Jakub", 19]

tekst = "Cześć mam na imię {0} i mam {1} lat. {0} O_o {1}".format(argument[0], argument[1])#podmiana {} na elementy z listy

print(tekst)

tekst2 = "Cześć mam na imię {0} i mam {1} lat.".format("Jakub", 19)#podmiana {} na tekst i liczbe
print(tekst2)

tekst = "Cześć mam na imię {imie}.".format(imie = argument[0])#tworzenie zmiennych, nie mieszać z podmianą na indexy listy

print(tekst)

