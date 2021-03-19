from pygame import *

init()
display.set_caption("Soldiers 2D")

windows = display.set_mode((1600, 900))


class Character():
    def __init__(self, x, y, facing, ch_radius, windows):
        self.x = x
        self.y = y
        self.facing = facing
        self.ch_radius = ch_radius
        self.windows = windows

    def draw(self, windows):
        draw.circle(self.windows, (255, 0, 255),
                    (self.x, self.y), self.ch_radius)

    def drawGun(self, windows):
        if self.facing == "N":
            draw.rect(self.windows, (0, 0, 0),
                      (self.x+self.ch_radius, self.y-150, 20, 150))

        if self.facing == "S":
            draw.rect(self.windows, (0, 0, 0),
                      (self.x-self.ch_radius-20, self.y, 20, 150))

        if self.facing == "E":
            draw.rect(self.windows, (0, 0, 0),
                      (self.x, self.y+self.ch_radius, 150, 20))

        if self.facing == "W":
            draw.rect(self.windows, (0, 0, 0),
                      (self.x-150, self.y-self.ch_radius-20, 150, 20))


def running():
    windows.fill((50, 50, 128))
    man.draw(windows)
    man.drawGun(windows)
    display.update()


vel = 10
man = Character(50, 50, "N", 100, windows)

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
        man.facing = "N"
    if keys[K_s]:
        man.y += vel
        man.facing = "S"
    if keys[K_a]:
        man.x -= vel
        man.facing = "W"
    if keys[K_d]:
        man.x += vel
        man.facing = "E"

    running()

quit()
