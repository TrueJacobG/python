t = int(input())

for test in range(t):
    i = [int(x) for x in input().split()]
    r = min(i[0], i[1])
    b = max(i[0], i[1])
    d = i[2]
    if b > (r*(d+1)):
        print("NO")
    else:
        print("YES")
