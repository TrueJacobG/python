import pygame
pygame.init()
pygame.display.set_caption("Third game!")

screen_width = 800
screen_height = 450

win = pygame.display.set_mode((screen_width, screen_height))

# stats


class player():
    def __init__(self, x, y, character_width, character_height):
        self.x = x
        self.y = y
        self.character_width = character_width
        self.character_height = character_height
        self.vel = 10
        self.isJump = False
        self.jumpHeight = 7
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(character, (self.x, self.y))


def drawGameWindows():
    win.blit(bg, (0, 0))
    man.draw(win)
    pygame.display.update()


walkRight = [pygame.image.load('character/1.png'),
             pygame.image.load('character/2.png'),
             pygame.image.load('character/3.png'),
             pygame.image.load('character/4.png'),
             pygame.image.load('character/5.png'),
             pygame.image.load('character/6.png'),
             pygame.image.load('character/7.png'),
             pygame.image.load('character/8.png'),
             pygame.image.load('character/9.png'),
             pygame.image.load('character/10.png'),
             ]

walkLeft = [pygame.transform.flip(pygame.image.load('character/1.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/2.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/3.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/4.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/5.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/6.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/7.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/8.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/9.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/10.png'), True, False)
            ]


bg = pygame.image.load('character/bg.png')
# ZROBIĆ
character = pygame.image.load('character/1.png')


clock = pygame.time.Clock()


man = player(10, 300, 100, 100)

# MAINLOOP
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < screen_width - man.character_width:
        man.x += man.vel
        man.left = False
        man.right = True
    else:
        man.left = False
        man.right = False
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            man.isJump = True
            helpy = man.y
            man.left = False
            man.right = False
    else:
        if man.jumpHeight >= -7:
            direction = 1
            if man.jumpHeight < 0:
                direction = -1
            man.y -= (man.jumpHeight ** 2) * direction
            if man.y < 0:
                man.y = helpy
                man.isJump = False
                man.jumpHeight = 7
            man.jumpHeight -= 1
        else:
            man.isJump = False
            man.jumpHeight = 7

    drawGameWindows()

pygame.quit()
