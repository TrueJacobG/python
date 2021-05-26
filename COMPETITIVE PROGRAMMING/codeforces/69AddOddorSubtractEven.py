import math

t = int(input())

for test in range(t):
    ab = [int(x) for x in input().split()]
    a = ab[0]
    b = ab[1]
    if math.fabs(b - a) == 0:
        print(0)
    else:
        if b > a:
            if (b - a) % 2 == 0:
                print(2)
            else:
                print(1)
        else:
            if (b-a) % 2 == 0:
                print(1)
            else:
                print(2)
