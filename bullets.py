import pygame
import main

BULLET_SPEED = 20
SPECIAL_SPEED = 15


class Bullet(pygame.sprite.Sprite):


    def __init__(self, x,y, side, type, i = 0):
        super().__init__()
        
        
        self.side = side
        self.speed = 0
        self.type = type
        self.i = i

        if type == "normal":
            if side == "friendly":
                self.image = pygame.transform.scale(main.BULLET,(15, 15))
                
                self.speed = BULLET_SPEED
            elif side == "enemy":
                self.speed = BULLET_SPEED / 2
                ene_laser = pygame.transform.scale(pygame.image.load('assets/ene_laser.png'), (15, 15))
                ene_laser2 = pygame.transform.scale(pygame.image.load('assets/ene_laser2.png'), (15, 15))
                ene_laser3 = pygame.transform.scale(pygame.image.load('assets/ene_laser3.png'), (15, 15))
                ene_laser4 = pygame.transform.scale(pygame.image.load('assets/ene_laser4.png'), (15, 15))
                self.animation_index = 0
                self.frames = [ene_laser, ene_laser2, ene_laser3, ene_laser4]
                self.image = self.frames[self.animation_index]
        elif type == "special":
            self.image = pygame.transform.scale(main.BULLET, (15, 15))
        self.rect = self.image.get_rect(center = (x, y))    

    def shots(self):
        if self.type == "normal" and self.side == "friendly":
            bullet = self.rect
            bullet.y -= self.speed
        elif self.type == 'normal' and self.side == 'enemy':
            bullet = self.rect
            bullet.y += self.speed
        elif self.type == 'special' and self.side == 'friendly':
            match self.i:
                case 0:  # NW
                    self.rect.x -= SPECIAL_SPEED
                    self.rect.y -= SPECIAL_SPEED
                case 1:  # N
                    self.rect.y -= SPECIAL_SPEED
                case 2:  # NE
                    self.rect.x += SPECIAL_SPEED
                    self.rect.y -= SPECIAL_SPEED
                case 3:  # E
                    self.rect.x += SPECIAL_SPEED
                case 4:  # SE
                    self.rect.x += SPECIAL_SPEED
                    self.rect.y += SPECIAL_SPEED
                case 5:  # S
                    self.rect.y += SPECIAL_SPEED
                case 6:  # SW
                    self.rect.y += SPECIAL_SPEED
                    self.rect.x -= SPECIAL_SPEED
                case 7:  # W
                    self.rect.x -= SPECIAL_SPEED



    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
        
    def update(self):
        self.shots()
        if self.side == "enemy":
            self.animation_state()
        self.destroy()

    def destroy(self):
        if (self.rect.y + self.rect.height > 720) or (self.rect.y < 0):
            self.kill()
        elif (self.rect.x + self.rect.width > 1000) or (self.rect.x < 0):
            self.kill()
