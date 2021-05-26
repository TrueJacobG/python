t = int(input())

for test in range(t):
    l = [int(x) for x in input().split()]
    n, m = l[0], l[1]
    if n == 1:
        print(0)
        continue
    if n == 2:
        print(m)
        continue
    print(2*m)
