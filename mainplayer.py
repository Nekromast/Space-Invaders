import pygame
import main

BULLET_SPEED = 20
WIDTH, HEIGHT = 1000, 720

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = main.PLAYERSHIP
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(WIDTH//2, HEIGHT//2, 40, 50)
        self.bullets = []
        self.special_bullets = []

    def player_input(self):
        keys = pygame.key.get_pressed()
        bullet = pygame.Rect(self.rect.x + self.rect.width // 2 + 5, self.rect.y, 5, 10)
        if keys[pygame.K_w] and self.rect.y - main.SPEED > 0:  # oben
            self.rect.y -= main.SPEED
        if keys[pygame.K_a] and self.rect.x + main.SPEED > 0:  # links
            self.rect.x -= main.SPEED
        if keys[pygame.K_s] and self.rect.y - main.SPEED < main.HEIGHT - self.rect.height * 2:  # unten
            self.rect.y += main.SPEED
        if keys[pygame.K_d] and self.rect.x + main.SPEED + self.rect.width * 2 < main.WIDTH:  # rechts
            self.rect.x += main.SPEED
        if keys[pygame.K_SPACE]:
            self.bullets.append(bullet)
            self.shoot()  # placeholder for shooting
        if keys[pygame.K_f]:
            self.special_bullets.append(bullet)
            self.shoot()

    def update(self):
        self.player_input()
        self.shoot()
        """self.movement()"""

    def shoot(self):
        for bullet in self.bullets:
            bullet.y -= BULLET_SPEED

        for bullet in self.special_bullets:
            i = self.special_bullets.index(bullet) % 9
            match i:
                case 0:  # NW
                    bullet.x -= 2
                    bullet.y -= 2
                case 1:  # N
                    bullet.y -= 2
                case 2:  # NE
                    bullet.x += 2
                    bullet.y -= 2
                case 3:  # E
                    bullet.x += 2
                case 4:  # SE
                    bullet.x += 2
                    bullet.y += 2
                case 5:  # S
                    bullet.y += 2
                case 6:  # SW
                    bullet.y += 2
                    bullet.x -= 2
                case 7:  # W
                    bullet.x -= 2
                case _:  # Default nach oben
                    bullet.y -= 2
