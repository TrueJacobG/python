n, m = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
l = sorted(l)
result = l[n-1] - l[0]
for i in range(1, m-n+1):
    if l[i+n-1]-l[i] < result:
        result = l[i+n-1]-l[i]
print(result)
