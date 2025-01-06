import random
from get_valid_columns import get_valid_columns
from is_terminal_node import is_terminal_node
from get_next_open_row import get_next_open_row
from update_board import update_board
from check_win import check_win

AI = 2
PLAYER = 1

def minimax(board, depth, maximizing_player):
    valid_columns = get_valid_columns(board)
    is_terminal = is_terminal_node(board)
    
    if depth == 0 or is_terminal:
        if is_terminal:
            if check_win(board, AI):
                return None, 1000000
            elif check_win(board, PLAYER):
                return None, -1000000
            else:
                return None, 0
        else:
            return None, 0

    if maximizing_player:
        value = -float('inf')
        best_column = random.choice(valid_columns)
        for col in valid_columns:
            row = get_next_open_row(board, col)
            temp_board = [row[:] for row in board]
            update_board(temp_board, row, col, AI)
            new_score = minimax(temp_board, depth - 1, False)[1]
            if new_score > value:
                value = new_score
                best_column = col
        return best_column, value
    else:
        value = float('inf')
        best_column = random.choice(valid_columns)
        for col in valid_columns:
            row = get_next_open_row(board, col)
            temp_board = [row[:] for row in board]
            update_board(temp_board, row, col, PLAYER)
            new_score = minimax(temp_board, depth - 1, True)[1]
            if new_score < value:
                value = new_score
                best_column = col
        return best_column, value
