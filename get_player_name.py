import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_HEIGHT = 700

def get_player_name(screen):
    font = pygame.font.SysFont("monospace", 40)
    screen.fill(BLACK)
    pygame.display.set_caption("Enter Player Name")

    input_box = pygame.Rect(100, SCREEN_HEIGHT // 2, 400, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    while True:
        screen.fill(BLACK)
        prompt_surface = font.render("Enter your name:", True, WHITE)
        screen.blit(prompt_surface, (100, SCREEN_HEIGHT // 2 - 100))
        pygame.draw.rect(screen, color, input_box, 2)
        text_surface = font.render(text, True, WHITE)
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                active = input_box.collidepoint(event.pos)
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    return text.strip()
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
