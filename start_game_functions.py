import pygame
from functions1 import events, update
from score_statistics import Statistics, Score
from space_ship import Spaceship
from ammo import update_ammo
from asteroid import set_asteroid_field, update_asteroids
from functions1 import load_end_window


def start_easy_game() -> None:
    pygame.init()

    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Shooter (Easy mode)")

    spaceship = Spaceship(screen)
    ammo = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    set_asteroid_field(screen=screen, asteroids=asteroids, speed1=3, speed2=15, count1=1, count2=30)
    statistics = Statistics()
    statistics.change_lifes(lifes=2)
    score_info = Score(screen, statistics)

    while True:
        events(screen=screen, spaceship=spaceship, ammo=ammo)

        if statistics.run_game:
            spaceship.update_spaceship()
            update(screen=screen, spaceship=spaceship, asteroids=asteroids, ammo=ammo, score=score_info)
            update_ammo(screen=screen, statistics=statistics, score=score_info,
                        asteroids=asteroids, ammo=ammo, total=25)
            update_asteroids(statistics=statistics, screen=screen, score=score_info, spaceship=spaceship,
                             asteroids=asteroids, ammo=ammo)
        elif statistics.lose:
            load_end_window(statistics.get_score())


def start_hard_game() -> None:
    pygame.init()

    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Shooter (Hard mode)")

    spaceship = Spaceship(screen)
    ammo = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    set_asteroid_field(screen=screen, asteroids=asteroids, speed1=5, speed2=19, count1=10, count2=30)
    statistics = Statistics()
    statistics.change_lifes(lifes=1)
    score_info = Score(screen, statistics)

    while True:
        events(screen=screen, spaceship=spaceship, ammo=ammo)

        if statistics.run_game:
            spaceship.update_spaceship()
            update(screen=screen, spaceship=spaceship, asteroids=asteroids, ammo=ammo, score=score_info)
            update_ammo(screen=screen, statistics=statistics, score=score_info, asteroids=asteroids, ammo=ammo,
                        total=15)
            update_asteroids(statistics=statistics, screen=screen, score=score_info, spaceship=spaceship,
                             asteroids=asteroids, ammo=ammo)
        elif statistics.lose:
            load_end_window(statistics.get_score())
