t = int(input())
for test in range(t):
    n = int(input())
    m = 1
    for k in range(1, 51):
        m = m * 2 + 1
        if n % m == 0:
            print(n//m)
            break
