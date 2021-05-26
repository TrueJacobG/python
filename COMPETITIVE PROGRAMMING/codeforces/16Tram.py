enter1 = input()

suma = 0
result = 0

for n in range(1, int(enter1)+1):
    enter2 = input().split()
    suma -= int(enter2[0])
    suma += int(enter2[1])
    if suma > result:
        result = suma

print(result)
