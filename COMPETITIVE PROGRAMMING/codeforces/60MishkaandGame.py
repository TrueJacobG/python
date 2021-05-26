t = int(input())

m = 0
c = 0

for x in range(t):
    result = [int(n) for n in input().split()]
    if result[0] > result[1]:
        m += 1
        continue
    if result[0] < result[1]:
        c += 1
        continue

if m > c:
    print("Mishka")
elif m < c:
    print("Chris")
else:
    print("Friendship is magic!^^")
