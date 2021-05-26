n = int(input())
teams = []
for i in range(0, n):
    teams.append(input().split(" "))

result = 0

for c in range(0, n):
    for x in range(0, n):
        if teams[c][0] == teams[x][1]:
            result += 1

print(result)
