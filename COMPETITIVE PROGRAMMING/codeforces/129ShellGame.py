n = int(input())
cups = [0, 0, 0]
cups[n-1] = 1
for _ in range(3):
    i1, i2 = (int(x)-1 for x in input().split())
    cups[i1], cups[i2] = cups[i2], cups[i1]

result = int(cups.index(1))
print(result+1)
