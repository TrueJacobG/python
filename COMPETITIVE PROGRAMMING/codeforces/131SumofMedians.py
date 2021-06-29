t = int(input())

for _ in range(t):
    n, k = (int(x) for x in input().split())
    a = [int(x) for x in input().split()]
    result = 0

    if n == 2:
        for i in range(0, len(a), 2):
            result += a[i]
        print(result)
        continue

    interval = (n+1)//2
    left = (n-interval)+1
    x = 1
    start = 0

    for i in range(len(a)-1, -1, -1):
        if x % left == 0:
            result += a[i]
            start += 1

        x += 1
        if start >= k:
            break
    print(result)
