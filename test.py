def isequal(l):
    return len(set(l)) <= 1


def GridColor(x, y):
    colors = [(229, 232, 53), (194, 196, 43), (164, 166, 36), (55, 237, 94),
              (47, 204, 81), (38, 166, 66), (54, 211, 235), (46, 181, 201), (39, 158, 176)]
    comp = [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9]]
    for i in range(3):
        for j in range(3):
            if j == x and i == y:
                return (j, i)


print(GridColor(2, 2))
