t = int(input())
l = [int(x) for x in input().split()]

flag = True
one = []
two = []
three = []

for c, element in enumerate(l):
    if element == 1:
        one.append(c+1)
    if element == 2:
        two.append(c+1)
    if element == 3:
        three.append(c+1)

min_len = min(len(one), len(two), len(three))
print(min_len)
for p in range(min_len):
    print(f"{one[p]} {two[p]} {three[p]}")
