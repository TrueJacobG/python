t = int(input())
l = [int(i) for i in input().split(" ")]

pol = 0
result = 0

for c in l:
    if c == -1 and pol > 0:
        pol -= 1
        continue
    if c == -1 and pol == 0:
        result += 1
        continue
    if c >= 1:
        pol += c

print(result)
