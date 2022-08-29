import main
import pygame
import os
from sys import exit
from random import randint, choice


class Enemy(pygame.sprite.Sprite):
    def __init__(self, shiptype):
        super().__init__()
        if self.ready == True:
            if shiptype == "ship":
                ene_ship = pygame.transform.rotate(pygame.image.load('assets/ship.png').convert_alpha(), 180)
                ene_ship = pygame.transform.scale(ene_ship, (70, 70))
                x_pos = randint(100, 620)
                self.ready = False
                self.spawn_time = pygame.time.get_ticks() + randint(1000, 2000)
                self.spawn_cooldown = 1000
            

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
      
    def spawn(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.spawn_time >= self.spawn_cooldown:
                self.ready = True 
        
    
    def update(self):
        self.spawn()
        self.rect.y += 5
        self.destroy()

    def destroy(self):
        if self.rect.y > 800 or self.rect.y < -100:
            self.kill()
