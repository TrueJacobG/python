n = int(input())
l = [int(x) for x in input().split()]
r1 = 0
r2 = 0
t = 1


while l:
    if len(l) == 1:
        if t == 1:
            r1 += l[0]
            l.pop(0)
            continue
        else:
            r2 += l[0]
            l.pop(0)
            continue

    if t == 1:
        if l[0] > l[len(l)-1]:
            r1 += l[0]
            l.pop(0)
            t = 2
            continue

        if l[0] < l[len(l)-1]:
            r1 += l[len(l)-1]
            l.pop(len(l)-1)
            t = 2
            continue

    else:
        if l[0] > l[len(l)-1] and t == 2:
            r2 += l[0]
            l.pop(0)
            t = 1
            continue

        if l[0] < l[len(l)-1] and t == 2:
            r2 += l[len(l)-1]
            l.pop(len(l)-1)
            t = 1
            continue


print(str(r1) + " " + str(r2))
