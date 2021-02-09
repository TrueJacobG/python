count = input()
colors = input()

colors = list(colors)
result = 0

for i in range(0, len(colors)-1):
    if colors[i] == colors[i+1]:
        result += 1

print(result)
