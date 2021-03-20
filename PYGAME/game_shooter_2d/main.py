from pygame import *

init()
display.set_caption("Soldiers 2D")

screen_width = 1600
screen_height = 900

windows = display.set_mode((screen_width, screen_height))


class Character():
    def __init__(self, x, y, facing, ch_radius, windows):
        self.x = x
        self.y = y
        self.facing = facing
        self.ch_radius = ch_radius
        self.windows = windows
        self.vel = 10
        self.gunSizeX = 20
        self.gunSizeY = 110

    def draw(self, windows):
        draw.circle(self.windows, (255, 0, 255),
                    (self.x, self.y), self.ch_radius)

    def drawGun(self, windows):
        if self.facing == "N":
            draw.rect(self.windows, (0, 0, 0),
                      (self.x+self.ch_radius, self.y-self.gunSizeY, self.gunSizeX, self.gunSizeY))

        if self.facing == "S":
            draw.rect(self.windows, (0, 0, 0),
                      (self.x-self.ch_radius-self.gunSizeX, self.y, self.gunSizeX, self.gunSizeY))

        if self.facing == "E":
            draw.rect(self.windows, (0, 0, 0),
                      (self.x, self.y+self.ch_radius, self.gunSizeY, self.gunSizeX))

        if self.facing == "W":
            draw.rect(self.windows, (0, 0, 0),
                      (self.x-self.gunSizeY, self.y-self.ch_radius-self.gunSizeX, self.gunSizeY, self.gunSizeX))


class Bullet():
    def __init__(self, x, y, facing, windows):
        self.x = x
        self.y = y
        self.facing = facing
        self.windows = windows
        self.vel = 25
        self.size = 10

    def shoot(self, windows):
        draw.circle(self.windows, (0, 0, 0), (self.x, self.y), self.size)


def running():
    windows.fill((50, 50, 128))
    man.draw(windows)
    man.drawGun(windows)
    for bullet in bullets:
        bullet.shoot(windows)
    display.update()


man = Character(300, 300, "N", 70, windows)
bullets = []

clock = time.Clock()
run = True
while run:
    clock.tick(60)

    for events in event.get():
        if events.type == QUIT:
            run = False

    for bullet in bullets:
        if bullet.facing == "E" and bullet.x <= screen_width:
            bullet.x += bullet.vel
        if bullet.facing == "W" and bullet.x >= 0:
            bullet.x -= bullet.vel
        if bullet.facing == "N" and bullet.y >= 0:
            bullet.y -= bullet.vel
        if bullet.facing == "S" and bullet.y <= screen_height:
            bullet.y += bullet.vel
        if bullet.x < 0 or bullet.x > screen_width or bullet.y < 0 or bullet.y > screen_height:
            bullets.pop(bullets.index(bullet))

    keys = key.get_pressed()

    if keys[K_w]:
        man.y -= man.vel
        man.facing = "N"
    if keys[K_s]:
        man.y += man.vel
        man.facing = "S"
    if keys[K_a]:
        man.x -= man.vel
        man.facing = "W"
    if keys[K_d]:
        man.x += man.vel
        man.facing = "E"

    if keys[K_SPACE]:
        if len(bullets) < 10:
            if man.facing == "N":
                bullets.append(Bullet(man.x+man.ch_radius+man.gunSizeX//2,
                                      man.y-man.gunSizeX, man.facing, windows))

            if man.facing == "S":
                bullets.append(Bullet(man.x-man.ch_radius-man.gunSizeX//2,
                                      man.y+man.gunSizeX, man.facing, windows))

            if man.facing == "W":
                bullets.append(Bullet(man.x-man.gunSizeX,
                                      man.y-man.ch_radius-man.gunSizeX//2, man.facing, windows))

            if man.facing == "E":
                bullets.append(Bullet(man.x+man.gunSizeX,
                                      man.y+man.ch_radius+man.gunSizeX//2, man.facing, windows))

    running()

quit()
