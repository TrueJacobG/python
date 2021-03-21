n = int(input())
levels = []

p = list(int(x) for x in input().split(" "))
q = list(int(x) for x in input().split(" "))

for i in range(1, n+1):
    levels.append(i)

del p[0]
del q[0]

result = []

for item in p + q:
    if item in result:
        continue
    else:
        result.append(item)

levels.sort()
result.sort()

if result == levels:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
