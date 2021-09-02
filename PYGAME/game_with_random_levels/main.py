import pygame as pg

pg.init()

# CONSTANTS
SIZE = 100
JUMPINGHEIGHT, FALLINGSPEED = 8, 1
WHITE, BLACK, RED, GREEN, BLUE = (
    255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)

s_width, s_height = 1600, 800
win = pg.display.set_mode((s_width, s_height))


clock = pg.time.Clock()


class Player():
    def __init__(self):
        # pos
        self.pos_x = 500
        self.pos_y = 599

        # size
        self.w_size = SIZE
        self.h_size = SIZE

        self.velocity = 10

        # jump
        self.isJump = False
        self.jumpHeight = JUMPINGHEIGHT

        self.fallingSpeed = FALLINGSPEED

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
                back = (self.jumpHeight ** 2) * direction
                self.pos_y -= (self.jumpHeight ** 2) * direction

                self.jumpHeight -= 1

                if self.collides():
                    print("COLLIDES")
                    self.pos_y += back

                if self.pos_y < 0:
                    self.pos_y = 600
                    self.isJump = False
                    self.jumpHeight = JUMPINGHEIGHT

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

    def fall(self):
        if not self.collides():
            self.pos_y += (self.fallingSpeed ** 2)
            self.fallingSpeed += 0.2
            if self.collides():
                self.fallingSpeed -= 0.2
                self.pos_y -= (self.fallingSpeed ** 2)
                self.fallingSpeed = FALLINGSPEED

    def move(self, keys, platforms):
        self.platforms = platforms
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.pos_x -= self.velocity
            if self.collides():
                self.pos_x += self.velocity

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.pos_x += self.velocity
            if self.collides():
                self.pos_x -= self.velocity

        self.crouch(keys)

        self.jump(keys)

        self.fall()

    def collides(self):
        for platform in self.platforms:
            if self.pos_x + self.w_size - 10 >= platform.x and self.pos_x <= platform.x + platform.width - 10 and self.pos_y + self.h_size >= platform.y and self.pos_y <= platform.y + platform.height:
                return True
        return False


class Platform():
    def __init__(self, character, x, y, width, height):
        self.character = character
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pg.draw.rect(win, GREEN, (self.x, self.y, self.width, self.height))


def updateWindow(platforms):
    win.fill(WHITE)
    for platform in platforms:
        platform.draw()
    character.drawCharacter()
    pg.display.update()


character = Player()
ground = Platform(character, 0, 700, 1600, 200)
platform1 = Platform(character, 200, 600, 100, 100)
platform2 = Platform(character, 450, 450, 100, 100)

platforms = [ground, platform1, platform2]

while True:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    character.move(pg.key.get_pressed(), platforms)

    updateWindow(platforms)
