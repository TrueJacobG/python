n, m = [int(x) for x in input().split()]
result = 0
day = 0
while n:
    day += 1
    n -= 1
    result += 1
    if day % m == 0:
        n += 1
print(result)
