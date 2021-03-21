enter = input().split()

a = int(enter[0])
b = int(enter[1])

result = 0

while 1 == 1:
    if a > b:
        print(result)
        break

    if a <= b:
        result += 1
        a = a*3
        b = b*2
