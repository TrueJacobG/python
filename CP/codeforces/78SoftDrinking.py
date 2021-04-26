li = [int(x) for x in input().split()]
n = li[0]
k = li[1]
l = li[2]
c = li[3]
d = li[4]
p = li[5]
nl = li[6]
np = li[7]

mililiters = (k * l)//nl
limes = c*d
salt = p//np

print(min(mililiters, limes, salt)//n)
