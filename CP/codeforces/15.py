enter = input().split()
n = int(enter[0])
k = int(enter[1])

for i in range(0, k):
    if n % 10 == 0:
        n //= 10
    else:
        n -= 1

print(n)
