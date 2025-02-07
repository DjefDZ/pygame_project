import pygame
from score_statistics import updating_new_best_score
from asteroid import set_asteroid_field
from score_statistics import Statistics, Score


class Ammo(pygame.sprite.Sprite):
    def __init__(self, screen, spaceship) -> None:
        super(Ammo, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 14, 35)
        self.color = 255, 50, 50
        self.rect.centerx = spaceship.rect.centerx
        self.rect.top = spaceship.rect.top
        self.y = float(self.rect.y)

    def update(self) -> None:
        self.y -= 1
        self.rect.y = self.y

    def draw_ammo(self, screen) -> None:
        pygame.draw.rect(screen, self.color, self.rect)


def update_ammo(screen, statistics: Statistics, score: Score, asteroids, ammo, total):
    ammo.update()
    for ammo1 in ammo.copy():
        if ammo1.rect.bottom <= 0:
            ammo.remove(ammo1)
    collisions = pygame.sprite.groupcollide(ammo, asteroids, True, True)
    if collisions:
        for asteroids in collisions.values():
            statistics.score += total
        score.show_cur_best_score()
        updating_new_best_score(statistics=statistics, score=score)
        score.show_left_lifes()
    if len(asteroids) == 0:
        ammo.empty()
        set_asteroid_field(screen=screen, asteroids=asteroids, speed1=3, speed2=15, count1=1, count2=30)
