t = int(input())

for test in range(t):
    lamps = [int(x) for x in input().split()]
    lamps.sort()
    if lamps[0] + lamps[1] + 1 >= lamps[2]:
        print("YES")
        continue
    print("NO")
