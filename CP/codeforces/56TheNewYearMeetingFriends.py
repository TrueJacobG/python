l = input().split(" ")
lint = []
for x in l:
    lint.append(int(x))

lint.sort()

result = lint[2] - lint[1]
result += lint[1] - lint[0]

print(result)
