import main
import spritesheet
import pygame
import os
from random import randint
import bullets

ss = spritesheet.spritesheet('assets/Enemies T1 Sprite Sheet from Carvel.png')
SHIP_SPEED = 5


class Enemy(pygame.sprite.Sprite):
    def __init__(self, shiptype):
        super().__init__()
        self.health = 5
        ene_ship = 0
        x_pos = 0
        self.type = shiptype
        self.ene_lasers = pygame.sprite.Group()
        self.ready = True
        self.shoot_time = 0

        if shiptype == "ship":
            ene_ship = pygame.transform.rotate(pygame.image.load('assets/ship.png').convert_alpha(), 180)
            ene_ship = pygame.transform.scale(ene_ship, (70, 70))
            x_pos = randint(100, main.WIDTH - 70)
            self.frames = [ene_ship]

        if shiptype == "ss_ship":
            ene_ship2 = pygame.image.load('assets/ene_ship2.png')
            ene_ship3 = pygame.image.load('assets/ene_ship3.png')
            ene_ship4 = pygame.image.load('assets/ene_ship4.png')

            ene_ship2 = pygame.transform.scale(ene_ship2, (70, 70))
            ene_ship3 = pygame.transform.scale(ene_ship3, (70, 70))
            ene_ship4 = pygame.transform.scale(ene_ship4, (70, 70))
            self.frames = [ene_ship2, ene_ship3, ene_ship4]
            x_pos = randint(70, main.WIDTH - 70)

        if shiptype == "ship_diag_LtoR":
            ene_ship2 = pygame.transform.rotate(pygame.image.load('assets/ene_ship2.png'), +45)
            ene_ship3 = pygame.transform.rotate(pygame.image.load('assets/ene_ship3.png'), +45)
            ene_ship4 = pygame.transform.rotate(pygame.image.load('assets/ene_ship4.png'), +45)

            ene_ship2 = pygame.transform.scale(ene_ship2, (70, 70))
            ene_ship3 = pygame.transform.scale(ene_ship3, (70, 70))
            ene_ship4 = pygame.transform.scale(ene_ship4, (70, 70))
            x_pos = 0
            self.frames = [ene_ship2, ene_ship3, ene_ship4]

        if shiptype == "ship_diag_RtoL":
            ene_ship2 = pygame.transform.rotate(pygame.image.load('assets/ene_ship2.png'), -45)
            ene_ship3 = pygame.transform.rotate(pygame.image.load('assets/ene_ship3.png'), -45)
            ene_ship4 = pygame.transform.rotate(pygame.image.load('assets/ene_ship4.png'), -45)

            ene_ship2 = pygame.transform.scale(ene_ship2, (70, 70))
            ene_ship3 = pygame.transform.scale(ene_ship3, (70, 70))
            ene_ship4 = pygame.transform.scale(ene_ship4, (70, 70))
            x_pos = main.WIDTH
            self.frames = [ene_ship2, ene_ship3, ene_ship4]

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.bullet_rect = (self.rect.x + self.rect.width / 2 - 10, self.rect.y + self.rect.height / 2 - 10, 20, 20)

    def movement(self, type):
        if type == 'ship' or 'ss_ship':
            self.rect.y += SHIP_SPEED

        if type == 'ship_diag_LtoR':
            self.rect.y += SHIP_SPEED / 2
            self.rect.x += SHIP_SPEED

        if type == 'ship_diag_RtoL':
            self.rect.y += SHIP_SPEED / 2
            self.rect.x -= SHIP_SPEED

    def update(self):
        self.movement(self.type)
        self.recharge()
        self.shoot()
        self.animation_state()
        self.ene_lasers.update()
        self.destroy()

    def destroy(self):
        if self.rect.y > 800 or self.rect.y < -100:
            self.kill()

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def shoot(self):
        bullet_rect = (self.rect.x + self.rect.width / 2 - 8, self.rect.y + self.rect.height, 20, 20)
        if self.ready:
            bullet = bullets.Bullet(bullet_rect, 'enemy', 'normal')
            self.ene_lasers.add(bullet)
            self.shoot_time = pygame.time.get_ticks()
            self.ready = False
            self.recharge()

    def recharge(self):
        if pygame.time.get_ticks() - self.shoot_time > 1000:
            self.ready = True
