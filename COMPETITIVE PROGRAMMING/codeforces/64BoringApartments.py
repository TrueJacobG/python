t = int(input())


def boring_numbers():
    result = []
    x = 1
    n = True
    while n:
        x = str(x)
        for i in range(1, 5):
            result.append(int(x*i))
        x = int(x) + 1
        if x == 10:
            n = False
    return result


l = boring_numbers()

for x in range(t):
    r = 0
    number = int(input())
    numberid = l.index(number)
    for i in range(numberid+1):
        r += len(str(l[i]))
    print(r)
