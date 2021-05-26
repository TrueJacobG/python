n = [int(x) for x in input().split()]
c1 = n[0]
c2 = n[1]
c3 = n[2]
c4 = n[3]

calories = 0

seq = list(input())
for element in seq:
    if element == "1":
        calories += c1
    if element == "2":
        calories += c2
    if element == "3":
        calories += c3
    if element == "4":
        calories += c4

print(calories)
