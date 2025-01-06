def save_game(player_name, board, turn):
    filename = f"{player_name}.txt"  # Save file using the player's name
    game_state = {'board': board, 'turn': turn}  # Create a dictionary with game data
    with open(filename, 'w') as file:
        file.write(str(game_state))  # Write the game state as a string
