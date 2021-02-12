enter1 = input().split()
enter2 = input()
enter2 = list(enter2)


n = int(enter1[0])
t = int(enter1[1])


for i in range(t, 0, -1):
    j = 0
    while(j < len(enter2)-1):
        if enter2[j] == 'B' and enter2[j+1] == 'G':
            enter2[j], enter2[j+1] = enter2[j+1], enter2[j]
            j += 1
        j += 1

print("".join(enter2))
