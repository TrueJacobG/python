t = int(input())

for _ in range(t):
    x = int(input())
    if len(str(x)) == 1:
        print(x)
        continue

    s = 0
    last = 9
    result = []

    while s < x and last > 0:
        result.append(min(x-s, last))
        s += last
        last -= 1

    if s < x:
        print(-1)
        continue
    print("".join(str(x) for x in sorted(result)))
