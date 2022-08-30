import pygame
import main

BULLET_SPEED = 20
SPECIAL_SPEED = 15


class Bullet(pygame.sprite.Sprite):

    def __init__(self, bullet_rect, side, type, i):
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
            else:
                self.speed = BULLET_SPEED
        else:
            pass

    def shots(self, type, i):
        if type == "normal":
            bullet = self.rect
            bullet.y += self.speed

        else:
            match i:
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

    def update(self):
        self.shots(self.type, self.i)
        self.destroy()

    def destroy(self):
        if (self.rect.y + self.rect.height > 720) or (self.rect.y < 0):
            self.kill()
        elif (self.rect.x + self.rect.width > 1000) or (self.rect.x < 0):
            self.kill()
