from math import fabs

t = int(input())


for test in range(t):
    n = int(input())
    s = [int(x) for x in input().split()]
    s.sort()
    mini = int(fabs(s[0]-s[1]))
    for i in range(len(s)-1):
        if fabs(s[i]-s[i+1]) < mini:
            mini = int(fabs(s[i]-s[i+1]))

    print(mini)
