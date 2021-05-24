t = int(input())

for test in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    e = 0
    o = 0
    for i, c in enumerate(a):
        if c % 2 != i % 2:
            if i % 2 == 0:
                e += 1
            else:
                o += 1

    if e != o:
        print(-1)
        continue

    print(e)

    # ok
