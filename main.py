
import os

import pygame

import enemies

import mainplayer

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
        pass
    def run(self):
        pass

def draw_window(player, e1):
    WINDOW.fill((0, 0, 0))  # black background

    WINDOW.blit(PLAYERSHIP, (player.rect.x, player.rect.y))
    WINDOW.blit(e1.image, (e1.rect.x, e1.rect.y))

    for bullet in player.bullets:
        WINDOW.blit(BULLET, (bullet.x, bullet.y))
    for bullet in player.special_bullets:
        WINDOW.blit(BULLET, (bullet.x, bullet.y))
    pygame.display.update()

def main():
    pygame.init()
    """player = pygame.Rect(WIDTH//2, HEIGHT//2, 40, 50)"""
    player = mainplayer.Player()
    """enemy1 = enemies.Enemy("ship")"""
    enemy1 = enemies.Enemy("ss_ship")
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        mainplayer.Player.update(player)
        enemies.Enemy.update(enemy1)

        draw_window(player, enemy1)


if __name__ == '__main__':
    main()
