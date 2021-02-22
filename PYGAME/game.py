import pygame
from player import player
from enemy import enemy
from bullets import knifes
from sounds import Music

pygame.init()
pygame.display.set_caption("Third game!")


screen_width = 800
screen_height = 450

win = pygame.display.set_mode((screen_width, screen_height))


SOUNDS = Music()


score = 0


def drawGameWindows():
    win.blit(bg, (0, 0))
    text = font.render("Score: " + str(score), 1, (0, 0, 0))
    win.blit(text, (640, 418))
    man.draw(win)
    enemy.drawEnemy(win)
    for bullet in bullets:
        bullet.drawKnife(win)
    pygame.display.update()


bg = pygame.image.load('character/bg.png')
# ZROBIĆ
character = pygame.image.load('character/1.png')


# MAINLOOP
man = player(10, 300, 100, 100, win, screen_width, screen_height)
enemy = enemy(200, 312, 100, 100, 400, win)
shootLoop = 0
bullets = []
font = pygame.font.SysFont('comicsans', 50)
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(30)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 10:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # colision -> enemy | character
    if enemy.visibility:
        if man.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and man.hitbox[1] + man.hitbox[3] > enemy.hitbox[1] + enemy.hitbox[3]:
            if man.hitbox[0] + man.hitbox[2] > enemy.hitbox[0] and man.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                SOUNDS.hit2Sound.play()
                man.hit()
                score -= 10

    # colision -> knife | enemy
    for bullet in bullets:
        if enemy.visibility:
            if bullet.y > enemy.hitbox[1] and bullet.y < enemy.hitbox[1] + enemy.hitbox[3]:
                if bullet.x + 40 > enemy.hitbox[0] and bullet.x < enemy.hitbox[0] + enemy.hitbox[2]:
                    SOUNDS.hitSound.play()
                    enemy.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))

        if bullet.x < screen_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        SOUNDS.knifeSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 10:
            bullets.append(knifes(
                round(man.x + man.character_width//3), round(man.y + man.character_height//2), facing, win))
        shootLoop = 1

    if keys[pygame.K_LEFT] or keys[pygame.K_a] and man.x > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and man.x < screen_width - man.character_width:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            SOUNDS.jumpSound.play()
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
