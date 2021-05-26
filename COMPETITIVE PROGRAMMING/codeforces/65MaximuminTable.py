n = int(input())


def sum_to_y(x, y, table):
    result = 1
    for i in range(y):
        result += table[x-1][i+1]
    return result


table = []

for x in range(n):
    table.append([])
    for y in range(n):
        if x == 0:
            table[x].append(1)
        else:
            if y == 0:
                table[x].append(1)
            else:
                table[x].append(sum_to_y(x, y, table))

print(table[n-1][n-1])
