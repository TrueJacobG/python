import operator

n = int(input())
s = input()

d = {}

for i in range(n-1):
    sub = s[i:i+2]
    if sub in d:
        d[sub] += 1
        continue
    d[sub] = 1

print(max(d.items(), key=operator.itemgetter(1))[0])
