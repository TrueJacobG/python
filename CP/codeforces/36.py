n = int(input())
soldiers2 = input().split(" ")
soldiers = []

for x in soldiers2:
    soldiers.append(int(x))

maxHeight = max(soldiers)
minHeight = min(soldiers)

result = 0
flag = True

while flag:

    for x in range(0, len(soldiers)):
        if int(soldiers[x]) == int(maxHeight):
            maxIndex = int(x)
            break

    for z in range(len(soldiers)-1, -1, -1):
        if int(soldiers[z]) == int(minHeight):
            minIndex = int(z)
            break

    #print(str(result)+" MAX "+str(maxIndex))
    #print(str(result)+" MIN "+str(minIndex))

    if maxIndex == 0 and minIndex == (len(soldiers)-1):
        flag = False
        break

    if maxIndex != 0:
        result += 1
        soldiers[maxIndex], soldiers[maxIndex -
                                     1] = soldiers[maxIndex-1], soldiers[maxIndex]
        continue

    elif minIndex != len(soldiers)-1:
        result += 1
        soldiers[minIndex], soldiers[minIndex +
                                     1] = soldiers[minIndex+1], soldiers[minIndex]


print(result)
