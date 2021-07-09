t = int(input())

for _ in range(t):
    a, b, n = (int(x) for x in input().split())
    result = 0
    if a > b:
        a, b = b, a

    while a <= n and b <= n:
        a += b
        result += 1
        if a > n:
            break
        b += a
        result += 1
        if b > n:
            break

    print(result)
