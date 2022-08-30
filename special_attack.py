import bullets
import pygame
import os

WIDTH, HEIGHT = 1000, 720
SHIPWIDTH, SHIPHEIGHT = 80, 100
SPEED = 5
BULLET_SPEED = 20
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BULLET = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'laserBullet.png')), (70, 70))


class SpecialAttack(pygame.sprite.Sprite):

    def __init__(self, bullet_rect, side):
        super().__init__()
        self.bulletlist = []
        for i in range(9):
            self.bulletlist.append(bullets.Bullet(bullet_rect, "friendly"))

    def shots(self, bullet, i):
        match i:
            case 0:  # NW
                bullet.rect.x -= 2
                bullet.rect.y -= 2
            case 1:  # N
                bullet.rect.y -= 2
            case 2:  # NE
                bullet.rect.x += 2
                bullet.rect.y -= 2
            case 3:  # E
                bullet.rect.x += 2
            case 4:  # SE
                bullet.rect.x += 2
                bullet.rect.y += 2
            case 5:  # S
                bullet.rect.y += 2
            case 6:  # SW
                bullet.rect.y += 2
                bullet.rect.x -= 2
            case 7:  # W
                bullet.rect.x -= 2
            case _:
                pass

    def update(self):
        for bullet in self.bulletlist:
            self.shots(bullet, self.bulletlist.index(bullet) % 8)
            bullet.destroy()
            WINDOW.blit(BULLET, (bullet.rect.x, bullet.rect.y))
            pygame.display.update()


