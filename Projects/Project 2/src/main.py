# --------
# @file     main.py
# @author   Taylor Martin
# @date     May 2023
# @class    CS 470 Artificial Intelligence
# @prof     Dr. Soule
# @project  Project 2: Connect 4
# @brief    This file contains the main application function.
# --------------------

# Imports
import sys
import interface
from game import Game

def main():
    """Main function"""

    colors = ('Blue', 'Green')

    game_interface = interface.CLI(colors)

    player_types = game_interface.get_players()

    game = Game(game_interface, colors, player_types)

    game.play()

if __name__ == "__main__":
    sys.exit(main())
    