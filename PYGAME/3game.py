import pygame
pygame.init()
pygame.display.set_caption("Third game!")

screen_width = 800
screen_height = 450

win = pygame.display.set_mode((screen_width, screen_height))

# stats

x = 10
y = screen_height - 120

character_w = 100
character_h = 100

vel = 10
isJump = False
jumpHeight = 7
left = False
right = False
walkCount = 0

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


def drawGameWindows():
    global walkCount
    win.blit(bg, (0, 0))
    if walkCount >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(character, (x, y))
    pygame.display.update()

    # MAINLOOP
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screen_width - character_w:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            helpy = y
            left = False
            right = False
    else:
        if jumpHeight >= -7:
            direction = 1
            if jumpHeight < 0:
                direction = -1
            y -= (jumpHeight ** 2) * direction
            if y < 0:
                y = helpy
                isJump = False
                jumpHeight = 7
            jumpHeight -= 1
        else:
            isJump = False
            jumpHeight = 7

    drawGameWindows()

pygame.quit()
