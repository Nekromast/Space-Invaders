import pygame
import os
import enemies
import special_attack
from player import Player

WIDTH, HEIGHT = 1000, 720
SHIPWIDTH, SHIPHEIGHT = 80, 100
SPEED = 5
BULLET_SPEED = 20
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

PLAYERSHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ship.png')), (SHIPWIDTH, SHIPHEIGHT))
BACKGROUND = pygame.image.load(os.path.join('assets', 'background.gif'))
BULLET = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'laserBullet.png')), (70, 70))


class Game:
    def __init__(self):
        player_sprite = Player()
        self.player = pygame.sprite.GroupSingle(player_sprite)

        enemies = pygame.sprite.Group()
    def run(self):
        pass
    
    
def shots(bullets, player):
    for bullet in bullets:
        bullet.y -= BULLET_SPEED


def draw_window(player, e1):
    WINDOW.fill((0, 0, 0))  # black background

    WINDOW.blit(PLAYERSHIP, (player.rect.x, player.rect.y))
    WINDOW.blit(e1.image, (e1.rect.x, e1.rect.y))

    for bullet in player.bullets:
        WINDOW.blit(BULLET, (bullet.rect.x, bullet.rect.y))

    pygame.display.update()


def main():
    pygame.init()
    player = Player()
    enemy1 = enemies.Enemy("ship")
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        Player.update(player)
        enemies.Enemy.update(enemy1)

        draw_window(player, enemy1)


if __name__ == '__main__':
    main()
