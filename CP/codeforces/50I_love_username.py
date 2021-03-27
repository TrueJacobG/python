n = int(input())
results = input().split(" ")

maxr = int(results[0])
minr = int(results[0])

score = 0

for r in range(0, n):
    if int(results[r]) > int(maxr):
        score += 1
        maxr = results[r]
    if int(results[r]) < int(minr):
        score += 1
        minr = results[r]

print(score)
