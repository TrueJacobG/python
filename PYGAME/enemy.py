import pygame


class enemy():
    def __init__(self, x, y, enemy_width, enemy_height, end, win):
        self.x = x
        self.y = y
        self.enemy_width = enemy_width
        self.enemy_height = enemy_height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 5

        self.win = win

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
        self.health = 100
        self.visibility = True

    def drawEnemy(self, win):
        self.move()
        if self.visibility:
            if self.walkCount >= 33:
                self.walkCount = 0

            if self.vel > 0:
                self.win.blit(
                    self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                self.win.blit(
                    self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(self.win, (255, 0, 0),
                             (self.hitbox[0], self.hitbox[1]-30, 50, 10))
            pygame.draw.rect(self.win, (0, 128, 0),
                             (self.hitbox[0], self.hitbox[1]-30, 50-(5 * (10-(self.health/10))), 10))
            self.hitbox = (self.x+30, self.y+8, 45, 80)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)

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
        if self.health > 0:
            self.health -= 10
        else:
            self.visibility = False
