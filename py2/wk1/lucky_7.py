#####################################################################################
#
# Name:   Ishai Masada
#
# Date:      1/25/22
#
# Purpose:  Show the user's probability disadvantage of Lucky Sevens
#
# Functions:       List of functions being called.
# Update:           If there updates made to the code, add the date and the update.
#
#####################################################################################

import random

# Store the player name and number of rolls
players = {}

for player in range(1, 5):

    max_funds = 0

    # Header in tabular format
    print("Welcome to Lucky Sevens!\n"
          "If the dice add up to 7, you gain $4.\n"
          "If they don\'t, then you lose $1.")

    player_name = input(f"\nYou are player {player}. Type in your name: ")

    # Initialize the pot value to be what the player is willing to bet
    pot = int(input(f"\nType in the amount of money you are willing to put in the pot: "))

    number_of_rolls = 0

    # Loop over the game sequence
    while pot > 0:
        # Check if the dice values add up to 7
        if sum([random.randint(1, 7) for _ in range(2)]) == 7:
            pot += 4
        else:
            pot -= 1

        # Assign the highest pot value to max_funds
        if max_funds < pot:
            max_funds = pot

        number_of_rolls += 1

    players[player_name] = number_of_rolls

    # Display the highest value of the pot in the game
    print(f"\nThis was the highest value of the pot in the game: {max_funds}")

    # Display the number of rolls it took yo empty the pot
    print(f"\nThis is the number of rolls it took the pot to empty: {number_of_rolls}")

# Name of the player with the most rolls in the game
most_rolls_name = max(players, key=players.get)
# Name of the player with the least rolls in the game
least_rolls_name = min(players, key=players.get)

# Display the name of the player with the largest amount of rolls
print(f"""\nThe player that had the largest amount of rolls: {most_rolls_name}
      Number of rolls they had: {players.get(most_rolls_name)}""")

# Display the name of the player with the least amount of rolls
print(f"""\nThe player that had the least amount of rolls: {least_rolls_name}
      Number of rolls they had: {players.get(least_rolls_name)} """)
