import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Moving square")


x = 150
y = 150

widthSquare = 100
heightSquare = 100
vel = 5

run = True

while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_UP]:
        y -= vel

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (10, 255, 10), (x, y, widthSquare, heightSquare))
    pygame.display.update()

pygame.quit()
