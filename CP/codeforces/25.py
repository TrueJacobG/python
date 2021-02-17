first = input().split()
n = int(first[0])
h = int(first[1])


a = input().split()
result = 0

for i in range(0, n):
    if int(a[i]) > h:
        result += 2
    else:
        result += 1

print(result)
