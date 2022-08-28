import main
import pygame
import os
from sys import exit
from random import randint,choice

class Enemy(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type =='ship':
            ene_ship = pygame.image.load('assets/ship.png').convert_alpha()
            
            x_pos = randint(0,720) 

            self.image = ene_ship
            self.rect = self.image.get_rect()
            
    def update(self):
        self.rect.y += 5
        if self.rect.y > 720:
            self.kill()
            
    def destroy(self):
        if self.rect.y > 800 or self.rect.y < -100:
            self.kill()