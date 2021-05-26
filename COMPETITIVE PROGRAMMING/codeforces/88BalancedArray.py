t = int(input())

for x in range(t):
    n = int(input())
    if n % 4 != 0:
        print("NO")
        continue
    print("YES")
    odd = []
    even = []
    for c in range(n+1):
        if c == n-1:
            odd.append(c+n//2)
            continue
        if c % 2 != 0:
            odd.append(c)
            continue
        if c % 2 == 0 and c != 0:
            even.append(c)
    even = even + odd
    s = ""
    for c in even:
        s += str(c)
        s += " "
    print(s)
