import timeit

import pygame
import main
import bullets
import time

import special_attack

BULLET_SPEED = 20
WIDTH, HEIGHT = 1000, 720


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = main.PLAYERSHIP
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 40, 50)
        self.bullets = []
        self.special_bullets = []

    def player_input(self):
        keys = pygame.key.get_pressed()
        bullet_rect = (self.rect.x + self.rect.width // 2 + 5, self.rect.y, 5, 10)

        if keys[pygame.K_w] and self.rect.y - main.SPEED > 0:  # oben
            self.rect.y -= main.SPEED
        if keys[pygame.K_a] and self.rect.x + main.SPEED > 0:  # links
            self.rect.x -= main.SPEED
        if keys[pygame.K_s] and self.rect.y - main.SPEED < main.HEIGHT - self.rect.height * 2:  # unten
            self.rect.y += main.SPEED
        if keys[pygame.K_d] and self.rect.x + main.SPEED + self.rect.width * 2 < main.WIDTH:  # rechts
            self.rect.x += main.SPEED
        if keys[pygame.K_SPACE]:
            self.bullets.append(bullets.Bullet(bullet_rect, "friendly"))
        if keys[pygame.K_f]:
            self.special_bullets.append(special_attack.SpecialAttack(bullet_rect, "friendly"))

    def update(self):
        self.player_input()
        self.shoot()

    def shoot(self):
        for bullet in self.bullets:
            bullet.update()

        for special in self.special_bullets:
            special.update()


