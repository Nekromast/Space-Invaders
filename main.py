import os
import pygame
import enemies
from player import Player
from sys import exit
from random import randint, choice

WIDTH, HEIGHT = 1000, 720
SHIPWIDTH, SHIPHEIGHT = 80, 100
SPEED = 5
BULLET_SPEED = 20
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

PLAYERSHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ship.png')), (SHIPWIDTH, SHIPHEIGHT))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background.jpg')), (WIDTH, HEIGHT))
BULLET = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'laserBullet.png')), (70, 70))


class Game:
    def __init__(self):
        pygame.mixer.pre_init(48000, 16, 2, 4096)
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Boi")
        self.clock = pygame.time.Clock()
        self.run = False
        self.start_time = 0
        self.score = 0

        # Groups
        player_sprite = Player(self.screen)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.ene_group = pygame.sprite.Group()


        # Intro Screen
        game_font = pygame.font.Font('freesansbold.ttf', 32)
        self.game_name = game_font.render('Space Boi', True, (255, 255, 255))
        self.game_name_rect = self.game_name.get_rect(center=(WIDTH / 2, HEIGHT  -200))

        self.game_message = game_font.render('Press Space to Start', True, (255, 255, 255))
        self.game_message_rect = self.game_message.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))
        # Timers
        self.enemy_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_timer, 1000)

    def run_game(self):
        # game loop
        while True:
            self.check_events()
            self.collision()
            self.update_screen()

    def collision(self):
        sound = pygame.mixer.Sound("assets/ha-gay_16.wav")
        for enemy in self.ene_group.sprites():
            for bullet in self.player.sprite.bullets.sprites():
                if pygame.sprite.collide_rect(bullet, enemy):
                    bullet.kill()
                    # ignore health warning
                    enemy.health -= 1
                    if enemy.health <= 0:
                        enemy.kill()
                        sound.play()

    def update_screen(self):

        if self.run:  # Stoppt als while nie (bisher ohne Condition)
            self.screen.fill('black')
            self.screen.blit(BACKGROUND, (0, 0))
            self.player.update()  # not a screen update, but a technical update
            self.ene_group.update()  # not a screen update, but a technical update
            self.player.draw(self.screen)
            self.ene_group.draw(self.screen)
            for ship in self.ene_group:
                ship.ene_lasers.draw(self.screen)
            self.player.sprite.bullets.draw(self.screen)  # sprite.bullets works!
        else:
            """self.screen.fill('black')"""
            self.screen.blit(BACKGROUND, (0, 0))
            self.screen.blit(self.game_name, self.game_name_rect)
            self.screen.blit(self.game_message, self.game_message_rect)

        pygame.display.update()
        self.clock.tick(60)
    # update all sprite groups
    # draw all sprite groups

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.run:
                if event.type == self.enemy_timer:
                    self.ene_group.add(enemies.Enemy(choice(["ss_ship", "ship"])))
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.run = True
                    self.start_time = pygame.time.get_ticks()

    # handle event loop


if __name__ == '__main__':
    space_game = Game()
    space_game.run_game()
