from pygame import *
import matrix

w_width, w_height = 1280, 720

init()

display.set_caption("Game of life!")
windows = display.set_mode((w_width, w_height))
clock = time.Clock()

scale = 20
offset = 1

matrix = matrix.matrix(w_width, w_height, scale, offset)
matrix.random_array()

run = True
while run:
    clock.tick(60)
    windows.fill((255, 255, 255))

    for e in event.get():
        if e.type == QUIT:
            run = False

    matrix.game_of_life(color_off=(255, 255, 255), window=windows)

    display.update()

quit()
