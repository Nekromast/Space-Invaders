import main
import spritesheet
import pygame
import os
from random import randint

ss = spritesheet.spritesheet('assets/Enemies T1 Sprite Sheet from Carvel.png')


class Enemy(pygame.sprite.Sprite):
    def __init__(self, shiptype):
        super().__init__()
        self.health = 5
        ene_ship = 0
        x_pos = 0

        if shiptype == "ship":
            ene_ship = pygame.transform.rotate(pygame.image.load('assets/ship.png').convert_alpha(), 180)
            ene_ship = pygame.transform.scale(ene_ship, (70, 70))
            x_pos = randint(100, main.WIDTH - 70)
            self.ready = False
            self.spawn_time = pygame.time.get_ticks() + randint(1000, 2000)
            self.spawn_cooldown = 1000

        if shiptype == "ss_ship":
            ene_ship = ss.image_at((7, 7, 18, 15))

        if shiptype == "ship_diag_LtoR":
            ene_ship = pygame.transform.rotate(pygame.image.load('assets/ship.png').convert_alpha(), -45)
            ene_ship = pygame.transform.scale(ene_ship, (70, 70))
            x_pos = 0

        if shiptype == "ship_diag_RtoL":
            ene_ship = pygame.transform.rotate(pygame.image.load('assets/ship.png').convert_alpha(), 45)
            ene_ship = pygame.transform.scale(ene_ship, (70, 70))
            x_pos = main.WIDTH - 70

        self.image = ene_ship
        self.rect = self.image.get_rect()
        self.rect.x = x_pos

    def update(self):
        self.rect.y += 5
        self.destroy()

    def destroy(self):
        if self.rect.y > 800 or self.rect.y < -100:
            self.kill()
