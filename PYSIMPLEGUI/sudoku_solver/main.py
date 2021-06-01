import PySimpleGUI as psg
import sys


# all themes -> psg.theme_previewer()
psg.theme("LightBlue")

table_inputs = []
for x in range(9):
    for y in range(9):
        table_inputs += [psg.In(size=(2, 1), font=("Arial", 30), key=(y, x))]

table_outputs = []
for x in range(9):
    for y in range(9):
        table_outputs += [psg.Text(key=(1, y, x),
                                   font=("Arial", 30), size=(2, 1))]

column1 = [
    [psg.Text("Type numbers:")],

    table_inputs[0:9],
    table_inputs[9:18],
    table_inputs[18:27],

    table_inputs[27:36],
    table_inputs[36:45],
    table_inputs[45:54],

    table_inputs[54:63],
    table_inputs[63:72],
    table_inputs[72:81],

    [psg.Button("Solve")],
]


column2 = [
    table_outputs[0:9],
    table_outputs[9:18],
    table_outputs[18:27],

    table_outputs[27:36],
    table_outputs[36:45],
    table_outputs[45:54],

    table_outputs[54:63],
    table_outputs[63:72],
    table_outputs[72:81],
]

layout = [[
    psg.Column(column1),
    psg.VSeparator(),
    psg.Column(column2, background_color='lightblue')
]]

window = psg.Window(title="Sudoku solver", layout=layout, margins=(10, 10))


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
    try:
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
        del grid
    except:
        return


grid = []

while True:
    event, value = window.read()

    if event == psg.WIN_CLOSED:
        break

    if event == "Solve":
        for x in range(9):
            row = []
            for y in range(9):
                if value[(y, x)] == "":
                    row.append(0)
                    continue
                row.append(int(value[(y, x)]))
            grid.append(row)

        solveSudoku()

        txt = open("grid_solved.txt", "r")
        t = txt.read()
        txt.close()

        solved_grid = []
        row = []
        for letter in t:
            if letter != "\n":
                row.append(letter)
                continue
            solved_grid.append(row)
            row = []

        for x in range(9):
            for y in range(9):
                window[(1, y, x)].update(solved_grid[x][y])

        # print(solved_grid)


window.close()
