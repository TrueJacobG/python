#dictionary

slownik = {1: "Poniedziałek", 2: "Wtorek", 3: "Środa", 4: "Czwartek", 7: "Niedziela"}
#index : wartość

print(slownik[1])#podajemy indexy
print(slownik[7])

slownik[5] = "Piątek"

slownik[6] = 6

slownik[8] = True

print(slownik)

slownik["a"] = "a"

print(slownik["a"])

print(slownik)


print(slownik.get(0, "To się wyświetli jak nie będzie indexu 0"))#jeśli jest to się wyświetli


for l in slownik:
    print(l)#zwróci indexy

print("$$$")

for l in slownik.keys():#da to samo
    print(l)

print("@@@")

for l in slownik.values():#wartości
    print(l)


slownik.pop(1)#usuwanie wartości z indexem 1

print(slownik)