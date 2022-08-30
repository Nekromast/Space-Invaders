import pygame
import main
import bullets

BULLET_SPEED = 20
WIDTH, HEIGHT = 1000, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = main.PLAYERSHIP
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 40, 50)
        self.bullets = pygame.sprite.Group()
        self.cd = pygame.time.get_ticks()
        self.ready = True

    def player_input(self):
        keys = pygame.key.get_pressed()
        bullet_rect = (self.rect.x + self.rect.width // 2 + 5, self.rect.y, 5, 10)
        if keys[pygame.K_w] and self.rect.y - main.SPEED > 0:  # oben
            self.rect.y -= main.SPEED
        if keys[pygame.K_a] and self.rect.x + main.SPEED > 0:  # links
            self.rect.x -= main.SPEED
        if keys[pygame.K_s] and self.rect.y - main.SPEED < main.HEIGHT - self.rect.height * 2:  # unten
            self.rect.y += main.SPEED
        if keys[pygame.K_d] and self.rect.x + main.SPEED + self.rect.width * 2 < main.WIDTH:  # rechts
            self.rect.x += main.SPEED
        if keys[pygame.K_SPACE] and self.ready:
            self.bullets.add(bullets.Bullet(bullet_rect, "friendly", "normal", None))
            self.ready = False
            self.cd = pygame.time.get_ticks()
        if keys[pygame.K_f] and self.ready:
            for i in range(8):
                self.bullets.add(bullets.Bullet(bullet_rect, "friendly", "special", i))
            self.cd = pygame.time.get_ticks()
            self.ready = False

    def update(self):
        self.cooldown()
        self.player_input()
        self.bullets.update()

    def cooldown(self):
        timer = pygame.time.get_ticks()

        if timer - self.cd >= 100:
            self.ready = True
