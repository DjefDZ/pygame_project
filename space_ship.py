import pygame
from load_image import load_image


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen) -> None:
        super(Spaceship, self).__init__()
        self.screen = screen
        self.image = load_image('spaceship.png', -1)
        self.image = pygame.transform.scale(self.image, (200, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.can_move_right = False
        self.can_move_left = False

    def draw_spaceship(self) -> None:
        self.screen.blit(self.image, self.rect)

    def update_spaceship(self) -> None:
        if self.can_move_right and self.rect.right < self.screen_rect.right:
            self.center += 0.5
        if self.can_move_left and self.rect.left > 0:
            self.center -= 0.5

        self.rect.centerx = self.center

    def create_spaceship(self) -> None:
        self.center = self.screen_rect.centerx
