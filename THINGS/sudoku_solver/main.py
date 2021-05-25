def getGridFromFile(filename="grid"):
    grid = []
    txt = open(filename + ".txt", "r")
    for line in txt.readlines():
        h = []
        for c in line:
            if c != "\n":
                h.append(int(c))
        grid.append(h)
    txt.close()
    return grid


def isValid(x, y, n, grid):
    for i in range(9):
        if grid[x][i] == n:
            return False
    for i in range(9):
        if grid[i][y] == n:
            return False

    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[x0+i][y0+j] == n:
                return False

    return True


def solveSudoku(g):
    grid = g
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if isValid(x, y, n, grid):
                        grid[x][y] = n
                        solveSudoku(grid)

    # TODO:

    for line in grid:
        for x in range(9):
            if line[x] == 0:
                solveSudoku(grid)

    return grid


def decor(g):
    g1 = g
    for line in g1:
        for i, item in enumerate(line):
            if i % 4 == 0:
                line.insert(i, "|")
        line.insert(13, "|")
    for x in range(0, 13, 4):
        g1.insert(x, "-------------")

    for line in g1:
        print(" ".join(str(x) for x in line))


if __name__ == '__main__':
    grid = getGridFromFile("grid")
    # it doesn't make sense but i cant do it in other way
    solved = solveSudoku(getGridFromFile("grid"))

    print("\n\n")
    print("UNSOLVED SUDOKU")
    decor(grid)

    print("SOLVED")
    decor(solved)
