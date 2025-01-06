import pygame
from get_player_name import get_player_name
from check_saved_game import check_saved_game
from prompt_continue_game import prompt_continue_game
from load_game import load_game
from initialize_board import initialize_board
from draw_board import draw_board
from game_loop import game_loop

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
PLAYER = 1

def main():
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create the game window
    pygame.display.set_caption("Connect 4")  # Set window title

    player_name = get_player_name(screen)  # Prompt for player's name

    # Load or start a new game based on the player's choice
    if check_saved_game(player_name):
        if prompt_continue_game(screen):
            board, turn = load_game(player_name)
            if board is None or turn is None:
                board = initialize_board()
                turn = PLAYER
        else:
            board = initialize_board()
            turn = PLAYER
    else:
        board = initialize_board()
        turn = PLAYER

    draw_board(screen, board)  # Draw the initial board
    game_loop(screen, board, player_name, turn)  # Start the game loop

# Run the game when the script is executed
if __name__ == "__main__":
    main()
