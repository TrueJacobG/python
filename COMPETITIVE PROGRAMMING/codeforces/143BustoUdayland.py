n = int(input())
bus = []
flag = 0
howMany = 1

for i in range(n):
    row = input()
    if row.find("OO") != -1 and howMany > 0:
        flag = 1
        howMany = 0
        for i in range(len(row)-1):
            if row[i] == "O" and row[i+1] == "O":
                row = row[:i] + "++" + row[i+2:]
                break
    bus.append(row)

if flag == 1:
    print("YES")
    for row in bus:
        print(row)
else:
    print("NO")
