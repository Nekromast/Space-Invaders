import main
import spritesheet
import pygame
import os
from sys import exit
from random import randint, choice

ss = spritesheet.spritesheet('assets/Enemies T1 Sprite Sheet from Carvel.png')


class Enemy(pygame.sprite.Sprite):
    def __init__(self, shiptype):
        super().__init__()

        if shiptype == "ship":
            ene_ship = pygame.transform.rotate(pygame.image.load('assets/ship.png').convert_alpha(), 180)
        if shiptype == "ss_ship":
            ene_ship = ss.image_at((7, 7, 18, 15)).convert_alpha()
        if shiptype == "ship" or "ss_ship":
            ene_ship = pygame.transform.scale(ene_ship, (70, 70))
            x_pos = randint(0, 720)

            self.image = ene_ship
            self.rect = self.image.get_rect()
            self.rect.x = x_pos

    def update(self):
        self.rect.y += 5
        if self.rect.y > 720:
            self.kill()

    def destroy(self):
        if self.rect.y > 800 or self.rect.y < -100:
            self.kill()
