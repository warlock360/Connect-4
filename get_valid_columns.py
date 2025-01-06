from is_valid_column import is_valid_column

COLS = 7

def get_valid_columns(board):
    return [c for c in range(COLS) if is_valid_column(board, c)]
