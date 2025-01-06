def load_game(player_name):
    filename = f"{player_name}.txt"  # Load file using the player's name
    try:
        with open(filename, 'r') as file:
            game_state = eval(file.read())  # Read and evaluate the saved data
            return game_state['board'], game_state['turn']
    except FileNotFoundError:
        return None, None  # Return None if the file doesn't exist
