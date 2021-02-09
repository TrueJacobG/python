table = ["Jeden", "Dwa"]
print(table[1])
print(table)

prawda = ["Jesteś", "super", "przystojniakiem!"]

i = 0
while i < len(prawda):#ilość elementow w liscie
    print(prawda[i])
    i += 1

prawda[1] = "giga"

i = 0
while i < len(prawda):#ilość elementow w liscie
    print(prawda[i])
    i += 1


tekst = "Hello world!"#zwykły string może być traktowany jak lista

print(tekst[0], tekst[1], tekst[2])


prawda += [" I to jest ", "prawda!"]#dodawanie do listy innej listy

print(prawda)

print(prawda * 2)#wyświetlanie pare razy


#metody

table.append("Trzy")

print(table)


table.append(["Cztery", "Pięć"])

print(table)#teraz jest jakby tablica w tablicy

print(table[3][1])#dołączona tablica jest jednym obiektem  a drugie [] odnosi się do tablicy w środku
#jest to lista 2d



table.insert(0, "Zero")#dodanie elementu na konkretnym miejscu

print(table)



print(table.count("Zero"))#liczy ilość elementow



print(table.index("Dwa"))#zwraca index tego elementu
#ps. wielkość liter ma znaczenie



table.remove("Trzy")

print(table)



lista = [1, 5, 87, -1, 9000]

print("Min: ", min(lista))
print("Max: ", max(lista))


lista.sort()#od najmniejszej do największej
print(lista)

table.reverse()#odwraca kolejnością
print(table)



lista.clear()
print(lista)