import math

dolars = int(input())

nominates = [100, 20, 10, 5, 1]
x = 0
result = 0

while dolars != 0:
    h = math.floor(dolars/nominates[x])
    dolars = dolars - nominates[x]*h
    result = result + 1*h
    x += 1

print(result)
