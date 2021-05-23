from pygame import *

init()
w_width, w_height = 900, 900
display.set_caption("Sudoku Solver")

window = display.set_mode((w_width, w_height))
clock = time.Clock()

window.fill([0, 255, 0])


def GridColor(x, y):
    colors = [(229, 232, 53), (194, 196, 43), (164, 166, 36), (55, 237, 94),
              (47, 204, 81), (38, 166, 66), (54, 211, 235), (46, 181, 201), (39, 158, 176)]
    comp = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for i in range(3):
        for j in range(3):
            if x in comp[j] and y in comp[i]:
                if j == 0:
                    return colors[i+j]
                if j == 1:
                    return colors[2+i+j]
                else:
                    return colors[4+i+j]


def drawGrid():
    for ix, x in enumerate(range(0, w_width, w_width//9)):
        for iy, y in enumerate(range(0, w_height, w_height//9)):
            rect = Rect(x, y, w_width//9, w_height//9, width=-1)
            draw.rect(window, GridColor(ix, iy), rect)
            for i in range(4):
                draw.rect(window, (255, 255, 255),
                          (x-i, y-i, w_width//9, w_height//9), 1)


def running(window):
    drawGrid()
    display.update()


run = True
while run:
    clock.tick(60)

    for e in event.get():
        if e.type == QUIT:
            run = False

    running(window)


quit()
