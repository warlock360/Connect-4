def check_saved_game(player_name):
    filename = f"{player_name}.txt"  # File name based on the player's name
    try:
        with open(filename, 'r'):
            return True  # File exists
    except FileNotFoundError:
        return False  # File doesn't exist
