number = int(input())
flag = False

while(not flag):
    number += 1
    newNumber = list(dict.fromkeys(list(str(number))))
    if len(newNumber) < 4:
        continue
    else:
        print(number)
        flag = True
