import pygame


class player():
    def __init__(self, x, y, character_width, character_height, win, screen_width, screen_height):
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

        self.win = win
        self.screen_width = screen_width
        self.screen_height = screen_height

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
                self.win.blit(
                    self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                self.win.blit(
                    self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                self.win.blit(self.walkRight[0], (self.x, self.y))
            else:
                self.win.blit(self.walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x+10, self.y+8, 80, 93)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)

    def hit(self):
        self.x = 10
        self.y = 300
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 80)
        text = font1.render('-10', 1, (0, 255, 255))
        self.win.blit(text, ((self.screen_width/2)-(text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while(i < 70):
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 71
                    pygame.quit()
