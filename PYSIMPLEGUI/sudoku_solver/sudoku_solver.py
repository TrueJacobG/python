import PySimpleGUI as psg

# all themes -> psg.theme_previewer()
psg.theme("LightBlue")


layout = [[
    [psg.Text("Type numbers:")],

    [
        [psg.In(size=(2, 1), font=("Arial", 30), key=(x, y)) for x in range(9)] for y in range(9)

    ],

    [psg.Button("Solve")],
    [psg.Button("Show")]
]]


window = psg.Window(title="Sudoku solver", layout=layout, margins=(10, 10))

grid = []

while True:
    event, value = window.read()

    if event == psg.WIN_CLOSED:
        break

    if event == "Solve":
        for x in range(9):
            row = []
            for y in range(9):
                row.append(value[(x, y)])
            grid.append(row)

    # TODO: we have grid!!!!

    if event == "Show":
        print(grid)

window.close()
