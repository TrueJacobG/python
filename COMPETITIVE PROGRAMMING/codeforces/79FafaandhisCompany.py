n = int(input())
s = 0

for x in range(1, n):
    if (n-x) % x == 0:
        s += 1

print(s)
