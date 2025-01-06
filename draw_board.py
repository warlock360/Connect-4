import pygame

ROWS = 6
COLS = 7
CELL_SIZE = 100
RADIUS = 40
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def draw_board(screen, board):
    screen.fill(BLUE)
    for r in range(ROWS):
        for c in range(COLS):
            pygame.draw.rect(screen, BLUE, (c * CELL_SIZE, (r + 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            color = BLACK
            if board[r][c] == 1:
                color = RED
            elif board[r][c] == 2:
                color = YELLOW
            pygame.draw.circle(screen, color, (c * CELL_SIZE + CELL_SIZE // 2, (r + 1) * CELL_SIZE + CELL_SIZE // 2), RADIUS)
    pygame.display.update()
