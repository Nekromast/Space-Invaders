import pygame
import main

BULLET_SPEED = 20


class Bullet(pygame.sprite.Sprite):

    def __init__(self, bullet_rect, side):
        super().__init__()
        self.image = main.BULLET
        self.rect = pygame.Rect(bullet_rect)
        self.bullets = []
        self.side = side
        if side == "friendly":
            pass
        if side == "enemy":
            pass

    def shots(self):
        bullet = self.rect
        bullet.y -= 2

    def update(self):
        self.shots()
        self.destroy()

    def destroy(self):
        if (self.rect.y > 720) or (self.rect.y < 0 + self.rect.height):
            del self
        elif (self.rect.x > 1000 + self.rect.width) or (self.rect.x < 0):
            del self
