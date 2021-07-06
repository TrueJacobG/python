from math import fabs

n = int(input())
x = [int(x) for x in input().split()]

for i in range(n):
    mi, mx = 0, 0
    if i == 0:
        mi = fabs(x[i] - x[i + 1])
        mx = fabs(x[i] - x[n-1])
        print(f"{int(mi)} {int(mx)}")
        continue

    if i == n - 1:
        mi = fabs(x[i] - x[i - 1])
        mx = fabs(x[i] - x[0])
        print(f"{int(mi)} {int(mx)}")
        continue

    mi = min(fabs(x[i]-x[i-1]), fabs(x[i]-x[i+1]))
    mx = max(fabs(x[i]-x[0]), fabs(x[i]-x[n-1]))
    print(f"{int(mi)} {int(mx)}")
