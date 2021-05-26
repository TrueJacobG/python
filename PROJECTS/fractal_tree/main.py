from pygame import *
from math import *

w_width, w_height = 900, 900

init()
display.set_caption("Fractal Tree!")
window = display.set_mode((w_width, w_height))
clock = time.Clock()

speed = 0.007


def FractalTree(pos, angle, value_z, value_n, direc, color=(0, 0, 0), depth=0):
    branch_factor = 0.30
    branch = value_z * branch_factor
    angle_x = branch * cos(direc)
    angle_y = branch * sin(direc)
    (x, y) = value_n
    pos_next = (x + angle_x, y + angle_y)
    draw.line(window, color, value_n, pos_next)

    if pos > 0:
        if depth == 0:
            color_f = (13, 60, 255)
            color_s = (150, 70, 255)
        else:
            color_s = color
            color_f = color

        new = value_z * (1 - branch_factor)
        FractalTree(pos-1, angle, new, pos_next,
                    direc-angle, color_s, depth+1)
        FractalTree(pos-1, angle, new, pos_next,
                    direc+angle, color_s, depth+1)


def main():
    angle = 0
    while True:
        clock.tick(60)
        for e in event.get():
            if e.type == QUIT:
                quit()

        angle += speed
        window.fill((0, 0, 0))
        FractalTree(9, angle, w_height * 0.9, (w_width//2, w_width-50), -pi/2)
        display.update()


if __name__ == '__main__':
    main()
    quit()
