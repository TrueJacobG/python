n = int(input())
p = list(input().split(" "))
result = 0

for i in range(0, n):
    result += int(p[i])


print(format(result/n, '.12f'))
