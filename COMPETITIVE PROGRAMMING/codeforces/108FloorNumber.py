t = int(input())

for test in range(t):
    n, x = [int(x) for x in input().split()]
    if n <= 2:
        print(1)
        continue
    print(((n-3)//x)+2)
