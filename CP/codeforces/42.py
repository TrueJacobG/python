t = int(input())
list = []
for i in range(t):
    list.append(int(input()))

for i in list:
    if i <= 2:
        print(0)
        continue
    if i % 2 == 0:
        print(i//2-1)
        continue
    print(i//2)
