COLS = 7
EMPTY = ' '

def is_valid_column(board, col):
    return 0 <= col < COLS and board[0][col] == EMPTY
