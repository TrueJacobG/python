t = int(input())

for _ in range(t):
    n = int(input())
    h = [int(x) for x in input().split()]

    arr_sum = 0
    arr_needed = 0

    for x in range(n):
        arr_needed += x
        arr_sum += h[x]
        if arr_sum < arr_needed:
            print("NO")
            break
    else:
        print("YES")
