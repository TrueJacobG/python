t = int(input())
for _ in range(t):
    dim = [int(y) for y in input().split()]
    a = dim[0]
    b = dim[1]
    x = a * 2
    y = b * 2
    if x > y:
        if a > y:
            print(a*a)
        else:
            print(y*y)
    else:
        if b > x:
            print(b*b)
        else:
            print(x*x)
