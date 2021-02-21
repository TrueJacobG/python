n = int(input())

magnets = []
for i in range(1, n+1):
    magnets.append(input())

groups = 1

for x in range(0, len(magnets)-1):
    if magnets[x] != magnets[x+1]:
        groups += 1

print(groups)
