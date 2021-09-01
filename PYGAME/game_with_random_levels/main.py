import pygame as pg

pg.init()

# CONSTANTS
SIZE = 100
JUMPINGHEIGHT = 8
WHITE, BLACK, BLUE = (255, 255, 255), (0, 0, 0), (0, 0, 255)

s_width, s_height = 1600, 800
win = pg.display.set_mode((s_width, s_height))


clock = pg.time.Clock()


class Player():
    def __init__(self):
        # pos
        self.pos_x = 50
        self.pos_y = 600

        # size
        self.w_size = SIZE
        self.h_size = SIZE

        self.velocity = 10

        # jump
        self.isJump = False
        self.jumpHeight = JUMPINGHEIGHT

        # crouch
        self.isCrouch = False

    def drawCharacter(self):
        pg.draw.rect(win, BLUE, (self.pos_x, self.pos_y,
                     self.w_size, self.h_size))

    def jump(self, keys):
        if not self.isJump:
            if keys[pg.K_UP] or keys[pg.K_w] or keys[pg.K_SPACE]:
                self.isJump = True
                self.startingY = self.pos_y
        else:
            if self.jumpHeight >= -JUMPINGHEIGHT:
                direction = 1
                if self.jumpHeight < 0:
                    direction = -1
                self.pos_y -= (self.jumpHeight ** 2) * direction
                if self.pos_y < 0:
                    self.pos_y = 600
                    self.isJump = False
                    self.jumpHeight = JUMPINGHEIGHT
                self.jumpHeight -= 1
            else:
                self.jumpHeight = JUMPINGHEIGHT
                self.isJump = False

    def crouch(self, keys):
        if not self.isCrouch:
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                self.isCrouch = True
                half = self.h_size//2
                self.h_size -= half
                self.pos_y += half
                self.crouchCounter = 0
        else:
            self.crouchCounter += 1
            if self.crouchCounter > 50:
                self.h_size *= 2
                self.pos_y -= self.h_size//2
                self.isCrouch = False

    def move(self, keys):
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.pos_x -= self.velocity

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.pos_x += self.velocity

        self.crouch(keys)

        self.jump(keys)


def updateWindow():
    win.fill(WHITE)
    character.drawCharacter()
    pg.display.update()


character = Player()

while True:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    character.move(pg.key.get_pressed())

    updateWindow()
