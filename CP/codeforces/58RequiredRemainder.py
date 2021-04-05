t = int(input())

l = []

for x in range(t):
    l.append([int(w) for w in input().split()])

for element in l:
    n = True
    if element[2] - (element[2] % element[0]) + element[1] <= element[2]:
        print(element[2] - (element[2] % element[0]) + element[1])
    else:
        print(element[2] - (element[2] % element[0]) - (element[0]-element[1]))
