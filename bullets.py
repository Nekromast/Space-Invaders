import pygame
import main

BULLET_SPEED = 20
SPECIAL_SPEED = 15


class Bullet(pygame.sprite.Sprite):


    def __init__(self, bullet_rect, side, type, i = 0):
        super().__init__()
        self.image = main.BULLET
        self.rect = pygame.Rect(bullet_rect)
        self.side = side
        self.speed = 0
        self.type = type
        self.i = i

        if type == "normal":
            if side == "friendly":
                self.speed = BULLET_SPEED * -1
            elif side == "enemy":
                self.speed = BULLET_SPEED     
                ene_laser = pygame.image.load('assets/ene_laser.png')
                ene_laser2 = pygame.image.load('assets/ene_laser2.png')
                ene_laser3 = pygame.image.load('assets/ene_laser3.png')
                ene_laser4 = pygame.image.load('assets/ene_laser4.png')
                self.animation_index = 0
                self.frames = [ene_laser, ene_laser2, ene_laser3, ene_laser4]
                self.image = self.frames[self.animation_index]
        else:
            pass
            

    def shots(self):
        if self.type == "normal" and self.side == "friendly":
            bullet = self.rect
            bullet.y += self.speed
        elif self.type == 'normal' and self.side == 'enemy':
            bullet = self.rect
            bullet.y -= self.speed
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
            self.animation_state
        self.destroy()

    def destroy(self):
        if (self.rect.y + self.rect.height > 720) or (self.rect.y < 0):
            self.kill()
        elif (self.rect.x + self.rect.width > 1000) or (self.rect.x < 0):
            self.kill()
