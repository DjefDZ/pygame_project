import pygame


def load_start_window():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)
    text = font.render("Играть", True, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 1)


def load_end_window(score):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)
    text1 = font.render("Вы проиграли", True, (255, 0, 20))
    text2 = font.render(f"Ваш счёт - {score}", True, (255, 0, 20))
    text1_x = width // 2 - text1.get_width() // 2
    text2_x = width // 2 - text2.get_width() // 2
    text1_y = height // 2 - text1.get_height() // 2 - 100
    text2_y = height // 2 - text2.get_height() // 2
    screen.blit(text1, (text1_x, text1_y))
    screen.blit(text2, (text2_x, text2_y))


def search_pos():
    pos = event.pos
    x_pos = pos[0]
    y_pos = pos[1]
    if 275 <= x_pos <= 525 and 255 <= y_pos <= 345:
        return True
    return False


if __name__ == '__main__':
    running = True
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    load_start_window()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if search_pos():
                    pass
        pygame.display.flip()
