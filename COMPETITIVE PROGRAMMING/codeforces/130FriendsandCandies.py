t = int(input())

for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    s = sum(l)
    av = s//n
    if s % n != 0:
        print(-1)
        continue
    result = 0
    for candies in l:
        if candies > av:
            result += 1
    print(result)
