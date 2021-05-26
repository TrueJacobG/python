t = int(input())

for x in range(t):
    time = [int(hm) for hm in input().split()]
    h = time[0]
    m = time[1]
    h = h * 60
    print(24*60-(h+m))
