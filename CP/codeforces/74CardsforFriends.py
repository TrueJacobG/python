t = int(input())

for x in range(t):
    items = [int(e) for e in input().split()]
    w = items[0]
    h = items[1]
    n = items[2]
    cards = 1
    while w % 2 == 0:
        w /= 2
        cards *= 2
    while h % 2 == 0:
        h /= 2
        cards *= 2
    if n <= cards:
        print("YES")
        continue
    else:
        print("NO")
        continue
