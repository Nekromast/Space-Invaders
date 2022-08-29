import pygame
import main


class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        self.image = main.BULLET
        self.rect = self.image.get_rect()
