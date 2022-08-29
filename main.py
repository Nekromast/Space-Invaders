import pygame
import os
import enemies
from player import Player

WIDTH, HEIGHT = 1000, 720
SHIPWIDTH, SHIPHEIGHT = 80, 100
SPEED = 5
BULLET_SPEED = 20
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

PLAYERSHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ship.png')), (SHIPWIDTH, SHIPHEIGHT))
BACKGROUND = pygame.image.load(os.path.join('assets', 'background.gif'))

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

def movement(keys_pressed, player):
    if keys_pressed[pygame.K_w] and player.y - SPEED > 0:  # oben
        player.y -= SPEED
    if keys_pressed[pygame.K_a] and player.x + SPEED > 0:  # links
        player.x -= SPEED
    if keys_pressed[pygame.K_s] and player.y - SPEED < HEIGHT - player.height*2:  # unten
        player.y += SPEED
    if keys_pressed[pygame.K_d] and player.x + SPEED + player.width*2 < WIDTH:  # rechts
        player.x += SPEED

def draw_window(player, bullets):
    WINDOW.fill((0, 0, 0)) # black background

    WINDOW.blit(PLAYERSHIP, (player.x, player.y))
    
    for bullet in bullets:
        pygame.draw.rect(WINDOW, (255, 0, 0), bullet)


    pygame.display.update()

def main():
    pygame.init()
    player = pygame.Rect(WIDTH//2, HEIGHT//2, 40, 50)
    health = 5
    bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(player.x + player.width - 2, player.y + 10, 5, 10)
                    bullets.append(bullet)
                
        shots(bullets, player)         
        keys_pressed = pygame.key.get_pressed()
        movement(keys_pressed, player)

        draw_window(player, bullets)

if __name__ == '__main__':
    main()
