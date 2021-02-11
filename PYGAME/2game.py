import pygame

pygame.init()

# date
x = 0
y = 0
squre_width = square_height = 100
vel = 5
screen_width = 800
screen_height = 450

win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Druga gra!")


run = True
isJump = False
jumpCount = 10

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # ctrl + l -> select current line

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= 1:
        x -= vel
    if keys[pygame.K_RIGHT] and x <= screen_width-squre_width-1:
        x += vel
    if not (isJump):
        if keys[pygame.K_UP] and y >= 1:
            y -= vel
        if keys[pygame.K_DOWN] and y <= screen_height-square_height-1:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            direction = 1
            if jumpCount < 0:
                direction = -1
            y -= (jumpCount ** 2) * 0.5 * direction
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((255, 255, 255))

    pygame.draw.rect(win, (0, 0, 0), (x, y, squre_width, square_height))

    pygame.display.update()

pygame.quit()
