t = int(input())
for test in range(t):
    n = int(input())
    s = str(input())
    c = s.count("0")
    if c == 1:
        print("BOB")
        continue
    elif c % 2 == 0:
        print("BOB")
        continue
    else:
        print("ALICE")
