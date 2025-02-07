import pygame
import sys
from ammo import Ammo
from score_statistics import Score


def events(screen, spaceship, ammo) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_ammo = Ammo(screen, spaceship)
                ammo.add(new_ammo)

            if event.key == pygame.K_RIGHT:
                spaceship.can_move_right = True
                spaceship.can_move_left = False

            if event.key == pygame.K_LEFT:
                spaceship.can_move_left = True
                spaceship.can_move_right = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                spaceship.can_move_right = False

            if event.key == pygame.K_LEFT:
                spaceship.can_move_left = False


def load_start_window(screen) -> None:
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)
    font1 = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 30)
    text = font.render("Играть", True, (100, 255, 100))
    text_easy = font1.render("Easy", True, (0, 255, 0))
    text_hard = font1.render("Hard", True, (255, 0, 0))
    text_press_enter = font2.render("Press <Enter> to start the game", True, (100, 100, 100))

    text_x = screen.get_width() // 2 - text.get_width() // 2
    text_y = screen.get_height() // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y - 50))
    screen.blit(text_easy, (text_x, text_y + 102))
    screen.blit(text_hard, (text_x + 148, text_y + 102))
    screen.blit(text_press_enter, (text_x - 40, text_y + 300))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 60, text_w + 20, text_h + 20), 1)
    pygame.draw.rect(screen, (0, 255, 0), (275, 360, 100, 50), 3)


def load_end_window(score) -> None:
    running = True
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)
    text1 = font.render("Game Over", True, (255, 0, 20))
    text2 = font.render(f"Your Score: {score}", True, (255, 0, 20))
    text1_x = width // 2 - text1.get_width() // 2
    text2_x = width // 2 - text2.get_width() // 2
    text1_y = height // 2 - text1.get_height() // 2 - 100
    text2_y = height // 2 - text2.get_height() // 2
    screen.blit(text1, (text1_x, text1_y))
    screen.blit(text2, (text2_x, text2_y))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        pygame.display.flip()


def search_pos(event) -> bool:
    pos = event.pos
    x_pos = pos[0]
    y_pos = pos[1]
    if 275 <= x_pos <= 525 and 255 <= y_pos <= 345:
        return True
    return False


def difficulty(screen, event) -> tuple:
    pos = event.pos
    x_pos = pos[0]
    y_pos = pos[1]
    if 275 <= x_pos <= 375 and 360 <= y_pos <= 410:
        pygame.draw.rect(screen, (0, 255, 0), (275, 360, 100, 50), 3)
        pygame.draw.rect(screen, (0, 0, 0), (425, 360, 100, 50), 3)
        return (True, 'easy')
    elif 425 <= x_pos <= 525 and 360 <= y_pos <= 410:
        pygame.draw.rect(screen, (0, 0, 0), (275, 360, 100, 50), 3)
        pygame.draw.rect(screen, (255, 0, 0), (425, 360, 100, 50), 3)
        return (True, 'hard')


def update(screen, spaceship, asteroids, ammo, score: Score) -> None:
    screen.fill((0, 0, 0))
    asteroids.draw(screen)
    spaceship.draw_spaceship()
    score.show_cur_best_score()
    score.show_score()
    score.show_left_lifes()
    for ammo1 in ammo.sprites():
        ammo1.draw_ammo(screen)

    pygame.display.flip()
