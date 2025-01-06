import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

def draw_win_message(screen, message):
    font = pygame.font.SysFont("monospace", 60, bold=True)
    text_surface = font.render(message, True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    pygame.draw.rect(screen, BLACK, text_rect.inflate(20, 20))
    screen.blit(text_surface, text_rect)
    pygame.display.update()

    pygame.time.wait(3000)
