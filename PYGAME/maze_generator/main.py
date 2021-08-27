import pygame as pg
from random import randint
import collections

pg.init()
pg.display.set_caption("Maze Generator")
s_width, s_height = 800, 640

win = pg.display.set_mode((s_width, s_height))

BLACK, WHITE, GREEN = (0, 0, 0), (255, 255, 255), (0, 255, 0)

win.fill(WHITE)


def findPath(arr, start, width, height):
    queue = collections.deque([[start]])
    seen = set([start])
    wall = 1
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if y == height-1:
            return path
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and arr[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


def createMaze(width, height):
    arr = []
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(randint(0, 1))
        arr.append(row)
    arr[0][0] = 0
    return arr


def drawMaze(arr):
    global win, BLACK, WHITE, GREEN
    size = 50
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                pg.draw.rect(win, WHITE, (j*50, 40+i*50, size, size))
            elif arr[i][j] == 1:
                pg.draw.rect(win, BLACK, (j*50, 40+i*50, size, size))
            else:
                pg.draw.rect(win, GREEN, (j*50, 40+i*50, size, size))


def addPathToMaze(arr, path):
    for step in path:
        y, x = step
        arr[x][y] = 2
    return arr


def printText(text):
    global win
    pg.font.init()
    font = pg.font.SysFont("Comic Sans MS", 40)
    text = "Generated mazes before create solvable maze -> " + str(text)
    textBoard = font.render(text, False, (0, 0, 0))
    win.blit(textBoard, (0, 0))


def main():
    unsolvable = 0
    while True:
        width, height = s_width//50, (s_height-40)//50
        arr = createMaze(width, height)
        path = findPath(arr, (0, 0), width, height)
        if path == None:
            unsolvable += 1
            continue
        break

    arr = addPathToMaze(arr, path)

    printText(unsolvable)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    pg.quit()

        drawMaze(arr)
        pg.display.update()


if __name__ == "__main__":
    main()
