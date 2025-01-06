import pygame
from draw_board import draw_board
from check_win import check_win
from minimax import minimax
from is_valid_column import is_valid_column
from get_next_open_row import get_next_open_row
from update_board import update_board
from draw_win_message import draw_win_message
from pause_menu import pause_menu
from save_game import save_game

PLAYER = 1
AI = 2
CELL_SIZE = 100

def game_loop(screen, board, player_name, turn):
    game_over = False  # Whether the game is over
    running = True  # Whether the loop should continue

    while not game_over and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game(player_name, board, turn)  # Save before exiting
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if not pause_menu(screen):  # Show pause menu and quit if chosen
                    save_game(player_name, board, turn)
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn == PLAYER:  # If it's the player's turn
                    col = event.pos[0] // CELL_SIZE  # Determine the column clicked
                    if is_valid_column(board, col):
                        row = get_next_open_row(board, col)
                        update_board(board, row, col, PLAYER)
                        draw_board(screen, board)  # Update board display
                        if check_win(board, PLAYER):  # Check for a win
                            draw_board(screen, board)  # Ensure latest board is shown
                            draw_win_message(screen, "You Win!")
                            running = False
                            break
                        turn = AI  # Switch to AI's turn

        if turn == AI and running:  # AI's turn
            pygame.time.wait(900)  # Small delay for AI move
            col, _ = minimax(board, 4, True)  # Get AI's move using minimax
            if is_valid_column(board, col):
                row = get_next_open_row(board, col)
                update_board(board, row, col, AI)
                draw_board(screen, board)
                if check_win(board, AI):  # Check if AI won
                    draw_board(screen, board)
                    draw_win_message(screen, "AI Wins!")
                    running = False
                    break
                turn = PLAYER  # Switch back to player's turn

    save_game(player_name, board, turn)  # Ensure the game state is saved before exiting
    pygame.quit()  # Quit pygame when the loop ends
