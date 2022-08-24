import pygame
import os

WIDTH, HEIGHT = 1000, 720
SHIPWIDTH, SHIPHEIGHT = 80, 100
SPEED = 5
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

PLAYERSHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ship.png')), (SHIPWIDTH, SHIPHEIGHT))
BACKGROUND = pygame.image.load(os.path.join('assets', 'background.gif'))

def movement(keys_pressed, player):
    if keys_pressed[pygame.K_w] and player.y - SPEED > 0:  # oben
        player.y -= SPEED
    if keys_pressed[pygame.K_a] and player.x + SPEED > 0:  # links
        player.x -= SPEED
    if keys_pressed[pygame.K_s] and player.y - SPEED < HEIGHT - player.height*2:  # unten
        player.y += SPEED
    if keys_pressed[pygame.K_d] and player.x + SPEED + player.width*2 < WIDTH:  # rechts
        player.x += SPEED

def draw_window(player):
    WINDOW.fill((0, 0, 0)) # black background

    WINDOW.blit(PLAYERSHIP, (player.x, player.y))


    pygame.display.update()

def main():
    player = pygame.Rect(WIDTH//2, HEIGHT//2, 40, 50)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        keys_pressed = pygame.key.get_pressed()
        movement(keys_pressed, player)

        draw_window(player)

if __name__ == '__main__':
    main()
