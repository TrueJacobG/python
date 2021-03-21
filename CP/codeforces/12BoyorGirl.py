name = input()

name = list(dict.fromkeys(name))

if len(name) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
