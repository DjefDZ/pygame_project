import pygame
from functions1 import load_start_window, difficulty
from start_game_functions import start_easy_game, start_hard_game

if __name__ == '__main__':
    running = True
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    load_start_window(screen=screen)
    diff = 'easy'
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                try:
                    if difficulty(screen=screen, event=event)[0]:
                        diff = difficulty(screen=screen, event=event)[1]
                except TypeError:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    if diff == 'easy':
                        start_easy_game()
                    else:
                        start_hard_game()
        pygame.display.flip()
