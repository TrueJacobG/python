t = int(input())

for x in range(t):
    n = int(input())
    l = [int(e) for e in input().split()]
    if sum(l) % 2 != 0:
        print("YES")
        continue
    else:
        flag1 = False
        flag2 = False
        for number in l:
            if number % 2 == 0:
                flag1 = True
            if number % 2 != 0:
                flag2 = True
        if flag1 and flag2:
            print("YES")
            continue
        print("NO")
