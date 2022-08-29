import pygame
import main

BULLET_SPEED = 20


class Bullet(pygame.sprite.Sprite):

    def __init__(self, rect, side):
        super().__init__()
        self.image = main.BULLET
        self.rect = rect
        self.bullets = []
        if side == "friendly":
            pass
        if side == "enemy":
            pass

    def shots(self):
        bullet = self.rect
        bullet.y -= BULLET_SPEED

    def update(self):
        self.shots()
