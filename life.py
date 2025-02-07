import pygame
from load_image import load_image


class Life(pygame.sprite.Sprite):
    def __init__(self, screen) -> None:
        super(Life, self).__init__()
        self.screen = screen
        self.image = load_image('heart.png', -1)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

    def draw_life(self) -> None:
        self.screen.blit(self.image, self.rect)
