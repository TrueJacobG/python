import pygame as pg
import time
from random import randint

pg.init()
pg.font.init()

# CONSTANTS
SIZE = 100
JUMPINGHEIGHT, FALLINGSPEED = 8, 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 127, 0)
GOLD = (255, 215, 0)


SCREENWIDTH, SCREENHEIGHT = 1280, 720
win = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT))


clock = pg.time.Clock()


class Player():
    def __init__(self):
        # pos
        self.level = 1

        # life
        self.deathCounter = 0

        # size
        self.characterWidth = SIZE
        self.characterHeight = SIZE

        # speed
        self.velocity = 10

        # jump
        self.isJump = False
        self.jumpHeight = JUMPINGHEIGHT
        self.jumpLimit = 0
        self.jumpSound = pg.mixer.Sound("jump.wav")
        pg.mixer.Sound.set_volume(self.jumpSound, 0.25)

        # fall
        self.fallingSpeed = FALLINGSPEED

        # crouch
        self.isCrouch = False

        # eq
        self.isEqActive = False
        self.eq = [[], [], []]
        self.delay = 0

    def main(self, keys, platforms):
        self.platforms = platforms

        self.fall()

        self.move(keys)

        self.crouch(keys)

        self.jump(keys)

        self.nextLevel()
        self.previousLevel()

    def respawn(self, x=55, y=599):
        self.posX = x
        self.posY = y

    def drawCharacter(self):
        pg.draw.rect(win, BLUE, (self.posX, self.posY,
                     self.characterWidth, self.characterHeight))

    def move(self, keys):
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.posX -= self.velocity
            if self.collides():
                self.posX += self.velocity

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.posX += self.velocity
            if self.collides():
                self.posX -= self.velocity

    def jump(self, keys):
        if not self.isJump:
            self.jumpLimit -= 1

        if not self.isJump:
            if keys[pg.K_UP] or keys[pg.K_w] or keys[pg.K_SPACE]:
                if self.jumpLimit <= 0:
                    self.isJump = True
                    self.jumpLimit = 17
                    self.jumpSound.play()

        else:
            if self.jumpHeight < 0:
                self.isJump = False
                self.jumpHeight = JUMPINGHEIGHT
            else:
                self.posY -= (self.jumpHeight ** 2)
                self.jumpHeight -= 1
                if self.collides():
                    while self.collides():
                        self.posY += 1
                    self.isJump = False
                    self.jumpHeight = JUMPINGHEIGHT

            # roof
            if self.posY < 0:
                self.posY = 0
                self.isJump = False
                self.jumpHeight = JUMPINGHEIGHT

    def crouch(self, keys):
        if not self.isCrouch:
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                self.isCrouch = True
                half = self.characterHeight//2
                self.characterHeight -= half
                self.posY += half
                self.crouchCounter = 0
        else:
            self.crouchCounter += 1
            if self.crouchCounter > 50:
                self.characterHeight *= 2
                self.posY -= self.characterHeight//2
                self.isCrouch = False
                if self.collides():
                    self.die()

    def fall(self):
        if not self.collides():
            self.posY += (self.fallingSpeed ** 2)
            self.fallingSpeed += 0.2
            if self.collides():
                self.fallingSpeed -= 0.2
                self.posY -= (self.fallingSpeed ** 2)
                self.fallingSpeed = FALLINGSPEED
                return False

    def collides(self):
        for platform in self.platforms:
            if self.posX + self.characterWidth - 10 >= platform.x and self.posX <= platform.x + platform.width - 10 and self.posY + self.characterHeight >= platform.y and self.posY <= platform.y + platform.height:
                if platform.isDamaging:
                    self.die()
                return True
        return False

    def nextLevel(self):
        if self.posX >= SCREENWIDTH - self.characterWidth//1.5:
            self.level += 1
            self.respawn()

    def previousLevel(self):
        if self.posX < 0:
            self.level -= 1
            self.respawn(x=SCREENWIDTH - 100)

    def printLevel(self):
        font = pg.font.SysFont("Times New Roman", 32)
        text = "LEVEL: " + str(self.level)
        textBoard = font.render(text, False, ORANGE)
        win.blit(textBoard, (SCREENWIDTH - 170 - 180, 0))

    def printDeaths(self):
        font = pg.font.SysFont("Times New Roman", 32)
        text = "DEATHS: " + str(self.deathCounter)
        textBoard = font.render(text, False, RED)
        win.blit(textBoard, (SCREENWIDTH - 170, 0))

    def die(self):
        self.respawn()
        self.deathCounter += 1

    def printEq(self, keys):
        self.delay -= 1
        if keys[pg.K_e] and self.delay <= 0:
            self.isEqActive = not self.isEqActive
            self.delay = 20

        if self.isEqActive:
            w = SCREENWIDTH//2
            h = SCREENHEIGHT//2
            size = 500

            squareSize = (size-1)//3
            border = 1

            pg.draw.rect(win, GOLD, (w-(size+80)//2,
                         h-(size+80)//2, size+80, size+80))

            pg.draw.rect(win, BLACK, (w-size//2,
                         h-size//2, size, size))

            for row in range(1, 4):
                for col in range(1, 4):
                    pg.draw.rect(win, WHITE, (w-(size//2) + (squareSize+border)*(row-1),
                                 h-(size//2) + (squareSize+border)*(col-1), squareSize, squareSize))


class Item():
    def __init__(self, name):
        self.name = name
        self.quality = randint(1, 5)


class Platform():
    def __init__(self, x, y, width, height, color=GREEN):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        if self.color == RED:
            self.isDamaging = True
        else:
            self.isDamaging = False

    def draw(self):
        pg.draw.rect(win, self.color,
                     (self.x, self.y, self.width, self.height))


class GameMap():
    def __init__(self):
        self.ground = Platform(0, 700, SCREENWIDTH, 200)
        self.wall = Platform(0, 0, 50, SCREENHEIGHT)
        self.platform1 = Platform(200, 600, 100, 100)
        self.platform2 = Platform(450, 450, 100, 100)
        self.platform3 = Platform(750, 250, 100, 100)

    def genPlatform(self, type="low", damage=False):
        if type == "low":
            y = randint(SCREENHEIGHT//2, SCREENHEIGHT-200)
        else:
            y = randint(0, SCREENHEIGHT//2)
        x = randint(200, SCREENWIDTH)
        width = randint(100, 500)
        height = randint(50, 200)
        if damage:
            return Platform(x, y, width, height, RED)
        return Platform(x, y, width, height)

    def generateMap(self):
        # TODO:
        platforms1 = [self.genPlatform("low", True), self.genPlatform("low")]
        platforms2 = [self.platform1, self.platform2, self.platform3]

        platforms1.append(self.ground)
        platforms1.append(self.wall)
        platforms2.append(self.ground)

        mp = [platforms1, platforms2]

        return mp


def updateWindow(keys, platforms):
    win.fill(WHITE)

    for platform in platforms:
        platform.draw()
    character.printLevel()
    character.printDeaths()
    character.drawCharacter()
    character.printEq(keys)

    pg.display.update()


character = Player()
character.respawn()

gameMap = GameMap()
mp = gameMap.generateMap()

while True:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    character.main(pg.key.get_pressed(), mp[character.level-1])

    updateWindow(pg.key.get_pressed(), mp[character.level-1])
