from math import fabs

t = int(input())

for x in range(t):
    n = int(input())
    l = sorted(set([int(e) for e in input().split()]))
    flag = "YES"
    for y in range(len(l)-1):
        if len(l) == 1:
            break
        if fabs(l[y] - l[y+1]) > 1:
            flag = "NO"
    print(flag)
