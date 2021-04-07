import pygame

pygame.init()

pygame.display.set_caption("Flappy Bird!")
w_width, w_height = 1600, 900
window = pygame.display.set_mode((w_width, w_height))
clock = pygame.time.Clock()

bg = pygame.image.load("bg.svg")
bgX = 0
bgX2 = bg.get_width()


class Player:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.jumpHeight = 8
        self.isJump = False

    def drawCharacter(self, screen):
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x, self.y), 50)


def running():
    window.blit(bg, (bgX, 0))
    window.blit(bg, (bgX2, 0))
    man.drawCharacter(window)
    pygame.display.update()


man = Player(500, 430, window)
speed = 60

run = True
while run:
    clock.tick(speed)

    bgX -= 3
    bgX2 -= 3
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if not man.isJump:
        if keys[pygame.K_SPACE]:
            man.isJump = True
            helpy = man.y
    else:
        if man.jumpHeight >= -8:
            direction = 1
            if man.jumpHeight < 0:
                direction = -1
            man.y -= (man.jumpHeight ** 2) * direction
            if man.y < 0:
                man.y = helpy
                man.isJump = False
                man.jumpHeight = 8
            man.jumpHeight -= 1
        else:
            man.isJump = False
            man.jumpHeight = 8

    running()

pygame.quit()
