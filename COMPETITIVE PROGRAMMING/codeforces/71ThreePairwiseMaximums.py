t = int(input())

for x in range(t):
    l = [int(e) for e in input().split()]
    l.sort()
    if l[1] != l[2]:
        print("NO")
        continue
    else:
        print("YES")
        print("{a} {b} {c}".format(a=l[0], b=l[0], c=l[2]))
