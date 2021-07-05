t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    if len(set(a)) == 1:
        print(-1)
        continue

    maxy = max(a)

    for i in range(0, len(a)):
        if a[i] == maxy:
            if i > 0 and a[i-1] != maxy:
                print(i+1)
                break
            if i < n-1 and a[i+1] != maxy:
                print(i+1)
                break
