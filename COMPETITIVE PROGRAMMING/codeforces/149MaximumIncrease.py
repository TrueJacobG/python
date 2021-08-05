n = int(input())
a = [int(x) for x in input().split()]

i = 0
gr1 = 1
gr2 = 1

while i < len(a)-1:

    if a[i] < a[i+1]:
        gr1 += 1
    else:
        gr2 = max(gr2, gr1)
        gr1 = 1

    i += 1
gr2 = max(gr2, gr1)
print(gr2)
