import pygame

def pause_menu(screen):
    font = pygame.font.SysFont("monospace", 40)
    screen.fill((0, 0, 0))  # Black background
    pygame.display.set_caption("Pause Menu")

    # Display the pause menu options
    prompt_surface = font.render("Paused", True, (255, 255, 255))
    resume_button = pygame.Rect(100, 200, 150, 50)
    quit_button = pygame.Rect(350, 200, 150, 50)
    pygame.draw.rect(screen, pygame.Color('green'), resume_button)
    pygame.draw.rect(screen, pygame.Color('red'), quit_button)
    resume_text = font.render("Resume", True, (255, 255, 255))
    quit_text = font.render("Quit", True, (255, 255, 255))
    screen.blit(prompt_surface, (200, 100))
    screen.blit(resume_text, (resume_button.x + 10, resume_button.y + 10))
    screen.blit(quit_text, (quit_button.x + 10, quit_button.y + 10))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.collidepoint(event.pos):
                    return True  # Resume the game
                if quit_button.collidepoint(event.pos):
                    return False  # Quit the game
