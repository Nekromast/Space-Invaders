import pygame
import main

BULLET_SPEED = 20


class Bullet(pygame.sprite.Sprite):

    def __init__(self, rect, side):
        super().__init__()
        self.image = main.BULLET
        self.rect = rect
        if side == "friendly":
           self.speed = BULLET_SPEED * -1 
        if side == "enemy":
            self.speed = BULLET_SPEED

    def shots(self):
        bullet = self.rect
        bullet.y += self.speed

    def update(self):
        self.shots()
