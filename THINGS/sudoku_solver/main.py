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


def isValid(row, column, number):
    global grid
    for i in range(0, 9):
        if grid[row][i] == number:
            return False
    for i in range(0, 9):
        if grid[i][column] == number:
            return False

    x0 = (row // 3) * 3
    y0 = (column // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x0+i][y0+j] == number:
                return False

    return True


def solveSudoku():
    global grid
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if isValid(row, column, number):
                        grid[row][column] = number
                        solveSudoku()
                        grid[row][column] = 0

                return

    with open("grid_solved.txt", "w") as f:
        for line in grid:
            f.write("".join(str(x) for x in line))
            f.write("\n")


def decorGrid(grid):
    for line in grid:
        for i in range(len(line)):
            if i % 4 == 0:
                line.insert(i, "|")
        line.insert(13, "|")
    for x in range(0, 13, 4):
        grid.insert(x, "-------------")

    for line in grid:
        print(" ".join(str(x) for x in line))


if __name__ == '__main__':
    grid_empty = getGridFromFile("grid")
    grid = getGridFromFile("grid")
    print("\n", "SUDOKU")
    decorGrid(grid_empty)

    print("\n", "SOLVED SUDOKU")
    solveSudoku()
    grid_solved = getGridFromFile("grid_solved")
    decorGrid(grid_solved)
