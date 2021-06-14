t = int(input())

for _ in range(t):
    n = int(input())
    while True:
        n /= 2
        if n == 1:
            print("NO")
            break
        if n < 1:
            print("YES")
            break
