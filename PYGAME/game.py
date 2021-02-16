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
        self.standing = True
        self.walkRight = [pygame.image.load('character/1.png'),
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
        self.walkLeft = [
            pygame.transform.flip(pygame.image.load(
                'character/1.png'), True, False),
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
        self.hitbox = (self.x+10, self.y+8, 80, 93)

    def draw(self, win):
        if self.walkCount >= 30:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(self.walkRight[0], (self.x, self.y))
            else:
                win.blit(self.walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x+10, self.y+8, 80, 93)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)


class enemy():
    def __init__(self, x, y, enemy_width, enemy_height, end):
        self.x = x
        self.y = y
        self.enemy_width = enemy_width
        self.enemy_height = enemy_height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 5
        self.walkRight = [pygame.image.load('character/1E.png'),
                          pygame.image.load('character/2E.png'),
                          pygame.image.load('character/3E.png'),
                          pygame.image.load('character/4E.png'),
                          pygame.image.load('character/5E.png'),
                          pygame.image.load('character/6E.png'),
                          pygame.image.load('character/7E.png'),
                          pygame.image.load('character/8E.png'),
                          pygame.image.load('character/9E.png'),
                          pygame.image.load('character/10E.png'),
                          pygame.image.load('character/11E.png')
                          ]
        self.walkLeft = [
            pygame.transform.flip(pygame.image.load(
                'character/1E.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/2E.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/3E.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/4E.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/5E.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/6E.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/7E.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/8E.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/9E.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/10E.png'), True, False),
            pygame.transform.flip(pygame.image.load(
                'character/11E.png'), True, False)
        ]
        self.hitbox = (self.x+10, self.y+8, 80, 93)

    def drawEnemy(self, win):
        self.move()
        if self.walkCount >= 33:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x+30, self.y+8, 45, 80)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        print("AUĆ!")
        pass


class knifes():
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 15 * facing
        self.bulletsImages = [pygame.image.load('character/knife.png'), pygame.transform.flip(
            pygame.image.load('character/knife.png'), True, False)]

    def drawKnife(self, win):
        if self.facing == 1:
            win.blit(self.bulletsImages[0], (self.x, self.y))
        else:
            win.blit(self.bulletsImages[1], (self.x, self.y))


def drawGameWindows():
    win.blit(bg, (0, 0))
    man.draw(win)
    enemy.drawEnemy(win)
    for bullet in bullets:
        bullet.drawKnife(win)
    pygame.display.update()


bg = pygame.image.load('character/bg.png')
# ZROBIĆ
character = pygame.image.load('character/1.png')


clock = pygame.time.Clock()

# MAINLOOP
man = player(10, 300, 100, 100)
enemy = enemy(200, 312, 100, 100, 400)
shootLoop = 0
bullets = []

run = True
while run:
    clock.tick(30)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 7:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y > enemy.hitbox[1] and bullet.y < enemy.hitbox[1] + enemy.hitbox[3]:
            if bullet.x + 40 > enemy.hitbox[0] and bullet.x < enemy.hitbox[0] + enemy.hitbox[2]:
                enemy.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < screen_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 3:
            bullets.append(knifes(
                round(man.x + man.character_width//3), round(man.y + man.character_height//2), facing))
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
