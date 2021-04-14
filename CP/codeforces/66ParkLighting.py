t = int(input())

for _ in range(t):
    h = [int(x) for x in input().split()]
    n = h[0]
    m = h[1]
    print((n*m+1)//2)
