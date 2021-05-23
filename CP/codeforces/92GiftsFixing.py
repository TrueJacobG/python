t = int(input())


for test in range(t):
    n = int(input())
    ar_a = [int(x) for x in input().split()]
    ar_b = [int(x) for x in input().split()]
    min_a = min(ar_a)
    min_b = min(ar_b)
    steps = 0
    for i in range(n):
        steps += max(ar_a[i] - min_a, ar_b[i] - min_b)
    print(steps)
