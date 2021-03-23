h = input().split(" ")
n = int(h[0])
k = int(h[1])

time = 240 - k
result = 0
# ups
for i in range(1, n+1):
    if time - (5*i) >= 0:
        time = time - (5*i)
        result += 1
    else:
        break

print(result)
