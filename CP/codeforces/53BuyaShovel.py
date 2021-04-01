l = input().split(" ")
k = int(l[0])
r = int(l[1])

n = True
result = 0
x = 1
while n:
    cost = (x * k)
    if str(cost-r)[-1] == "0" or str(cost)[-1] == "0":
        result = x
        n = False
        break
    x += 1


print(result)
