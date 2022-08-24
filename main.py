import pygame
import os

WIDTH, HEIGHT = 1000, 720
SHIPWIDTH, SHIPHEIGHT = 80, 100
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

PLAYERSHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ship.png')), (SHIPWIDTH, SHIPHEIGHT))
BACKGROUND = pygame.image.load(os.path.join('assets', 'background.gif'))

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

        draw_window(player)

if __name__ == '__main__':
    main()
