t = int(input())

for x in range(t):
    n = int(input())
    l = [str(y) for y in range(n, 0, -1)]
    llen = len(l)
    if llen % 2 == 0:
        print(" ".join(l))
    else:
        c = llen//2
        l[c], l[llen-1] = l[llen-1], l[c]
        print(" ".join(l))
