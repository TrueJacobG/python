t = int(input())

for test in range(t):
    n = int(input())
    res = len(str(n))
    print(9*(res-1)+n//(int('1'*res)))
