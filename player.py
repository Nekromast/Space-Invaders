import pygame
import os
import main

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = main.PLAYERSHIP
        self.rect = self.image.get_rect()
        
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y - main.SPEED > 0:  # oben
            self.rect.y -= main.SPEED
        if keys[pygame.K_a] and self.rect.x + main.SPEED > 0:  # links
            self.rect.x -= main.SPEED
        if keys[pygame.K_s] and self.rect.y - main.SPEED < main.HEIGHT - self.rect.height*2:  # unten
            self.rectself.rect.y += main.SPEED
        if keys[pygame.K_d] and self.rect.x + main.SPEED + self.rect.width*2 < main.WIDTH:  # rechts
            self.rect.x += main.SPEED
        if keys[pygame.K_SPACE]:
            self.shoot() #placeholder for shooting
        
    def update(self):
        self.movement()