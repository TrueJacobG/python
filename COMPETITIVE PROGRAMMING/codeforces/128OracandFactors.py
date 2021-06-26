t = int(input())


for _ in range(t):
    n, k = (int(x) for x in input().split())
    if n % 2 == 0:
        print(n+2*k)
        continue
    h = 0
    for i in range(n, 1, -1):
        if n % i == 0:
            h = i
    print(n+h+2*(k-1))
