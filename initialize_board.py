ROWS = 6
COLS = 7
EMPTY = ' '

def initialize_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
