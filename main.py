import os
import pygame
import enemies
from player import Player
from sys import exit
from random import randint, choice

WIDTH, HEIGHT = 1000, 720
SHIPWIDTH, SHIPHEIGHT = 80, 100
SPEED = 7
BULLET_SPEED = 20
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

PLAYERSHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ship.png')), (SHIPWIDTH, SHIPHEIGHT))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background.jpg')), (WIDTH, HEIGHT))
BULLET = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'laserBullet.png')), (70, 70))


class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 4096)
        pygame.mixer.init()
        pygame.mixer.fadeout(200)
        pygame.init()
        self.screen = WINDOW
        pygame.display.set_caption("Space Boi")
        self.clock = pygame.time.Clock()
        self.run = False
        self.start_time = 0
        self.score = 0
        self.health = 10

        # Groups
        player_sprite = Player(self.screen)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.ene_group = pygame.sprite.Group()

        # Intro Screen
        self.game_font = pygame.font.Font('freesansbold.ttf', 32)
        self.game_name = self.game_font.render('Space Boi', True, (255, 255, 255))
        self.game_name_rect = self.game_name.get_rect(center=(WIDTH / 2, HEIGHT - 200))

        self.game_message = self.game_font.render('Press Space to Start', True, (255, 255, 255))
        self.game_message_rect = self.game_message.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))
        # Timers
        self.enemy_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_timer, 750)

    def run_game(self):
        # game loop
        while True:
            self.check_events()
            self.enemy_collision()
            self.player_collision()
            self.update_screen()

    def enemy_collision(self):
        sound = pygame.mixer.Sound("assets/pew.ogg")
        for enemy in self.ene_group.sprites():
            for bullet in self.player.sprite.bullets.sprites():
                if pygame.sprite.collide_rect(bullet, enemy):
                    bullet.kill()
                    sound.play().set_volume(0.25)
                    # ignore health warning
                    enemy.health -= 1
                    if enemy.health <= 0:
                        enemy.kill()
                        self.score += 5

    def player_collision(self):
        for ship in self.ene_group:
            for lasers in ship.ene_lasers:
                if pygame.sprite.collide_rect(lasers, self.player.sprite):
                    lasers.kill()
                    self.health -= 1
                    if self.health <= 0:
                        self.run = False
                        
    def reset(self):
        self.health = 10
        self.score = 0
        for ship2 in self.ene_group:
            ship2.ene_lasers.empty()
        self.ene_group.empty()
        self.player.sprite.bullets.empty()

    def update_screen(self):

        if self.run:  # Stoppt als while nie (bisher ohne Condition)
            self.screen.fill('black')
            self.screen.blit(BACKGROUND, (0, 0))
            # Health and Score bar
            healthtext = self.game_font.render("Health: " + str(self.health), True, (255, 255, 255))
            scoretext = self.game_font.render("Score: " + str(self.score), True, (255, 255, 255))
            self.screen.blit(healthtext, (10, HEIGHT - 60))
            self.screen.blit(scoretext, (WIDTH - 200, HEIGHT - 60))

            self.player.update()
            self.ene_group.update()
            self.player.draw(self.screen)
            self.ene_group.draw(self.screen)
            for ship in self.ene_group:
                ship.ene_lasers.draw(self.screen)
            self.player.sprite.bullets.draw(self.screen)  # sprite.bullets works!
        else:
            """self.screen.fill('black')"""
            score_message = self.game_font.render(f'Score: {self.score}', False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center=(WIDTH / 2, HEIGHT * 0.25))
            self.screen.blit(BACKGROUND, (0, 0))
            self.screen.blit(self.game_name, self.game_name_rect)
            self.screen.blit(self.game_message, self.game_message_rect)
            
            if self.score > 0:
                self.screen.blit(score_message, score_message_rect)
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
                    self.ene_group.add(enemies.Enemy(choice(["ss_ship"])))
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.run = True
                    self.start_time = pygame.time.get_ticks()
                    self.reset()

    # handle event loop


if __name__ == '__main__':
    space_game = Game()
    space_game.run_game()
