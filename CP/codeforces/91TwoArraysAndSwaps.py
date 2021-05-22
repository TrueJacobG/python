t = int(input())

for test in range(t):
    h = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    for move in range(h[1]):
        ai = a.index(min(a))
        bi = b.index(max(b))
        if min(a) > max(b):
            break
        a[ai], b[bi] = b[bi], a[ai]
    print(sum(a))
