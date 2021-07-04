t = int(input())

for _ in range(t):
    s = [int(x) for x in input().split()]
    final = sorted([max(s[0], s[1]), max(s[2], s[3])])
    maxies = sorted(s)[2:]
    if final == maxies:
        print("YES")
    else:
        print("NO")
