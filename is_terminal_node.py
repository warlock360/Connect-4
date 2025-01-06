from check_win import check_win
from get_valid_columns import get_valid_columns

PLAYER = 1
AI = 2

def is_terminal_node(board):
    return check_win(board, PLAYER) or check_win(board, AI) or len(get_valid_columns(board)) == 0
