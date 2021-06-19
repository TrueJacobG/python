t = int(input())

for _ in range(t):
    hp, va, ls = [int(x) for x in input().split()]
    for first in range(va):
        if hp//2+10 > hp:
            break
        hp = hp//2+10
    for second in range(ls):
        hp -= 10
    if hp <= 0:
        print("YES")
        continue
    print("NO")
