t = int(input())

for test in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(len(set(a)))
