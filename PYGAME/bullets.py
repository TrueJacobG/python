import pygame


class knifes():
    def __init__(self, x, y, facing, win):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 15 * facing

        self.win = win

        self.bulletsImages = [pygame.image.load('character/knife.png'), pygame.transform.flip(
            pygame.image.load('character/knife.png'), True, False)]

    def drawKnife(self, win):
        if self.facing == 1:
            self.win.blit(self.bulletsImages[0], (self.x, self.y))
        else:
            self.win.blit(self.bulletsImages[1], (self.x, self.y))
