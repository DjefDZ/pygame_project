import pygame
import random
from load_image import load_image
from score_statistics import Statistics, Score


class Asteroid(pygame.sprite.Sprite):

    def __init__(self, screen, size) -> None:
        super(Asteroid, self).__init__()
        self.screen = screen
        self.image = load_image('asteroid.png', -1)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_asteroids(self) -> None:
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        self.y += self.speed
        self.rect.y = self.y

    def set_speed(self, speed=0.05) -> None:
        self.speed = speed


def update_asteroids(screen, statistics, score, spaceship, asteroids, ammo) -> None:
    asteroids.update()
    if pygame.sprite.spritecollideany(spaceship, asteroids):
        spaceship_kill(screen=screen, statistics=statistics, score=score, spaceship=spaceship, asteroids=asteroids,
                       ammo=ammo)
    asteroids_check(screen=screen, statistics=statistics, score=score, spaceship=spaceship, asteroids=asteroids,
                    ammo=ammo)


def asteroids_check(screen, statistics, score, spaceship, asteroids, ammo) -> None:
    screen_rect = screen.get_rect()
    for asteroid in asteroids.sprites():
        if asteroid.rect.bottom >= screen_rect.bottom:
            spaceship_kill(screen=screen, statistics=statistics, score=score, spaceship=spaceship, asteroids=asteroids,
                           ammo=ammo)
            break


def set_asteroid_field(screen, asteroids, speed1, speed2, count1, count2) -> None:
    for _ in range(random.randint(count1, count2)):
        asteroid = Asteroid(screen, random.randint(35, 100))
        asteroid.set_speed(random.randint(speed1, speed2) / 100)
        asteroid.x = random.randint(126, 700 - 125)
        asteroid.y = random.randint(-1000, 0)
        asteroid.rect.x = asteroid.x
        asteroid.rect.y = asteroid.rect.height
        asteroids.add(asteroid)


def spaceship_kill(screen, statistics: Statistics, score: Score, spaceship, asteroids, ammo) -> None:
    if statistics.spaceships_left > 0:
        statistics.spaceships_left -= 1
        spaceship.create_spaceship()
        score.show_left_lifes()
        asteroids.empty()
        ammo.empty()
        set_asteroid_field(screen, asteroids, 3, 13, 1, 30)
    else:
        statistics.run_game = False
        statistics.lose = True
