n = int(input())

result = 0
for i in range(0, n):
    pandq = input().split()
    if int(pandq[0]) + 2 <= int(pandq[1]):
        result += 1

print(result)
