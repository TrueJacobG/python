q = int(input())

for test in range(q):
    l1 = [int(x) for x in input().split()]
    n = l1[0]
    k = l1[1]
    a = [int(x) for x in input().split()]
    if (max(a)-min(a)) > k:
        if (max(a)-min(a) > 2*k):
            print(-1)
            continue
        if min(a) + k > max(a) - k:
            print(min(a)+k)
            continue
        else:
            print(max(a)-k)
            continue
    else:
        print(min(a)+k)
        continue
