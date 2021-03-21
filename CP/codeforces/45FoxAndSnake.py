n = input().split(" ")

rows = int(n[0])
columns = int(n[1])

string = ""

startDot = [x for x in range(1, 51, 4)]
lastDot = [x for x in range(3, 51, 4)]

for x in range(rows):
    for y in range(columns):
        if x % 2 != 0:
            if x in startDot:
                if y != columns-1:
                    string += "."
                    continue
                else:
                    string += "#"
                    continue

            if x in lastDot:
                if y != 0:
                    string += "."
                    continue
                else:
                    string += "#"
                    continue

            else:
                string += "#"
                continue
        else:
            string += "#"
            continue
    print(string)
    string = ""
