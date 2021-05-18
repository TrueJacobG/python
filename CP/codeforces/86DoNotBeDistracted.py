t = int(input())

for x in range(t):
    n = int(input())
    tasks = [str(l) for l in input()]
    for y in range(0, n-1):
        if tasks[y] == tasks[y+1]:
            tasks[y] = 0
    tasks = list(filter(lambda x: x != 0, tasks))
    flag = "YES"
    for task in tasks:
        if tasks.count(task) > 1:
            flag = "NO"
    print(flag)
