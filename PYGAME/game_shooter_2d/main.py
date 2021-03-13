from pygame import *

init()
display.set_caption("Soldiers 2D")

windows = display.set_mode((1600, 900))


class Character():
    def __init__(self, x, y, ch_radius, windows):
        self.x = x
        self.y = y
        self.ch_radius = ch_radius
        self.windows = windows

    def draw(self, windows):
        draw.circle(self.windows, (255, 0, 255),
                    (self.x, self.y), self.ch_radius)


def running():
    windows.fill((0, 0, 0))
    man.draw(windows)
    display.update()


vel = 10
man = Character(50, 50, 100, windows)

clock = time.Clock()
run = True
while run:
    clock.tick(60)

    for events in event.get():
        if events.type == QUIT:
            run = False

    keys = key.get_pressed()

    if keys[K_w]:
        man.y -= vel
    if keys[K_s]:
        man.y += vel
    if keys[K_a]:
        man.x -= vel
    if keys[K_d]:
        man.x += vel

    running()

quit()
