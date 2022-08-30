import pygame
import main

BULLET_SPEED = 20


class Bullet(pygame.sprite.Sprite):

    def __init__(self, bullet_rect, side):
        super().__init__()
        self.image = main.BULLET
        self.rect = pygame.Rect(bullet_rect)
        self.side = side
        if side == "friendly":
           self.speed = BULLET_SPEED * -1
        if side == "enemy":
            self.speed = BULLET_SPEED

    def shots(self):
        bullet = self.rect
        bullet.y += self.speed

    def update(self):
        self.shots()
        self.destroy()

    def destroy(self):
        if (self.rect.y > 720) or (self.rect.y < 0 + self.rect.height):
            del self
        elif (self.rect.x > 1000 + self.rect.width) or (self.rect.x < 0):
            del self
