from math import factorial

n = int(input())
floors = 0
fact = 1
summary = 0


while n > 0:
    for x in range(fact+1):
        summary += x
    fact += 1
    if summary > n:
        break
    floors += 1


print(floors)
