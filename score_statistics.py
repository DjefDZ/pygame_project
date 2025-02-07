import pygame
from life import Life


class Score:
    def __init__(self, screen, statistics) -> None:
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.statistics = statistics
        self.font = pygame.font.SysFont(None, 36)
        self.show_score()
        self.show_best_score()
        self.show_cur_best_score()
        self.show_left_lifes()

    def show_score(self) -> None:
        self.score_img = self.font.render(str(self.statistics.get_score()), True, (0, 150, 0), (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 50

    def show_best_score(self) -> None:
        self.high_score_image = self.font.render(str(self.statistics.best_score), True, (255, 0, 0), (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = 20

    def show_left_lifes(self) -> None:
        self.lifes = pygame.sprite.Group()
        for spaceship_number in range(self.statistics.spaceships_left):
            life = Life(self.screen)
            life.rect.x = 0 + spaceship_number * life.rect.width
            life.rect.y = 0
            self.lifes.add(life)

    def show_cur_best_score(self) -> None:
        self.show_left_lifes()
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.lifes.draw(self.screen)


class Statistics:

    def __init__(self) -> None:
        self.spaceships_left = 0
        self.score = 0

        self.run_game = True
        self.lose = False

        with open('best_score.txt') as file:
            self.best_score = int(file.readline())

    def lifes_and_scores(self) -> None:
        self.spaceships_left = 0
        self.score = 0

    def change_lifes(self, lifes: int) -> None:
        self.spaceships_left = lifes

    def get_score(self) -> int:
        return self.score

    def get_lifes(self) -> int:
        return self.spaceships_left

    def get_best_score(self) -> int:
        return self.best_score


def updating_new_best_score(statistics: Statistics, score: Score) -> None:
    if statistics.score > statistics.best_score:
        statistics.best_score = statistics.score
        score.show_best_score()
        with open('best_score.txt', 'w') as file:
            file.write(str(statistics.best_score))
