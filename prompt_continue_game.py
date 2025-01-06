import pygame
ROWS = 6  # Number of rows in the Connect 4 grid
COLS = 7  # Number of columns in the Connect 4 grid
CELL_SIZE = 100  # Pixel size for each cell in the grid
RADIUS = 40  # Radius of the circles representing player and AI moves
SCREEN_WIDTH = COLS * CELL_SIZE  # Total width of the screen
SCREEN_HEIGHT = (ROWS + 1) * CELL_SIZE  # Screen height, including space for messages
PLAYER = 1  # Representing the human player
AI = 2  # Representing the AI player
EMPTY = ' '  # Placeholder for empty cells in the grid

# Colors in RGB format for the game elements
BLUE = (0, 0, 255)  # Background of the grid
BLACK = (0, 0, 0)  # Empty slots in the grid
RED = (255, 0, 0)  # Player's pieces
YELLOW = (255, 255, 0)  # AI's pieces
WHITE = (255, 255, 255)  # Text color for messages
def prompt_continue_game(screen):
    font = pygame.font.SysFont("monospace", 40)
    screen.fill(BLACK)
    pygame.display.set_caption("Continue Game")

    # Prompt text and buttons
    prompt_surface = font.render("Continue previous game?", True, WHITE)
    yes_button = pygame.Rect(100, SCREEN_HEIGHT // 2, 150, 50)
    no_button = pygame.Rect(350, SCREEN_HEIGHT // 2, 150, 50)
    pygame.draw.rect(screen, pygame.Color('green'), yes_button)
    pygame.draw.rect(screen, pygame.Color('red'), no_button)
    yes_text = font.render("Yes", True, WHITE)
    no_text = font.render("No", True, WHITE)
    screen.blit(prompt_surface, (100, SCREEN_HEIGHT // 2 - 100))
    screen.blit(yes_text, (yes_button.x + 50, yes_button.y + 10))
    screen.blit(no_text, (no_button.x + 50, no_button.y + 10))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button.collidepoint(event.pos):
                    return True  # Continue the game
                if no_button.collidepoint(event.pos):
                    return False  # Start a new game