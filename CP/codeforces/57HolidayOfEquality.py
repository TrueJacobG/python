t = int(input())
welfares = [int(i) for i in input().split()]
max_welfares = max(welfares)
result = 0
for wel in welfares:
    result += max_welfares-wel
print(result)
