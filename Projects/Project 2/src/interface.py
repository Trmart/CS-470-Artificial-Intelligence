# --------
# @file     interface.py
# @author   Taylor Martin
# @date     May 2023
# @class    CS 470 Artificial Intelligence
# @prof     Dr. Soule
# @project  Project 2: Connect 4
# @brief    This file contains the interface class.
# --------------------

# Imports
import sys
import argparse

class Interface:
    """
    This class represents a game interface. It must be overridden by the child class.
    
    
    Attributes:
        colors (list): The list of colors.
        options (list): The list of options.
    """

    def __init__(self, colors):
        """
        The constructor for the interface class. It initializes the interface.
        
        Parameters:
            colors (list): The list of colors.
        """
        
        self.colors = colors
        self.options = self.parseArgs()

    def parseArgs(self):
        """
        This function parses the arguments.
        
        Returns:
            The parsed arguments.
        """
        
        parser = argparse.ArgumentParser(description='Connect 4')
        
        parser.add_argument(
            '--solo', dest = 'players', action='store_const', const = ['Human', 'Computer'], help='Play against the computer'
            )
        
        parser.add_argument(
            '--versus', dest = 'players', action='store_const', const = ['Human', 'Human'], help='Play against another human'
            )
        
        parser.add_argument(
            '--auto', dest = 'players', action='store_const', const = ['Computer', 'Computer'], help='Watch the two computers play against each other'
            )
        
        return parser.parse_args()
    
    def  print_board(self, board):
        """
        This function prints the board. It must be overridden by the child class."""
        raise NotImplementedError("print_board not implemented")
    
    def ask_for_player_move(self, color):
        """
        This function asks for the player move. It must be overridden by the child class.
        """
        raise NotImplementedError("ask_for_player_move not implemented")
    
class CLI(Interface):
    """
    This class represents a command line interface.
    
    Attributes:
        colors (list): The list of colors.
        options (list): The list of options.
        ask_for_player_move_message (str): The message to ask for the player move.
        
    """
    def __init__(self, colors):
        super().__init__(colors)
        self.ask_for_player_move_message = "Player {}, please enter a column number: "

    def get_players(self):
        """
        This function gets the players.
        
        Returns:
            The players.
        """
        
        players = self.options.players
        
        if players is None:
            players = ['Human', 'Human']
        
        return players
    
    def get_player_game_piece(self, color):
        """
        This function gets the player game piece.
        
        Parameters:
            color (str): The color to check.
        
        Returns:
            The player game piece.
        """
        
        if color == self.colors[0]:
            return 'O'
        if color == self.colors[1]:
            return 'X'

    def first_player_selection_prompt(self, players):
        """
        This function prompts for the first player.
        
        Parameters:
            players (list): The list of players.
            
        Returns:
            The first player.
        """
        
        color_string = "Which player shall go first: {} or {}? "
        
        try:
            input_ = input(color_string.format(
                players[0].color, players[1].color))
        except KeyboardInterrupt:
            self._exit()
        
        if input_ == 'exit':
            self._exit()
        
        for player in players:
            if input_ == player.color:
                return player
        
        if input_ == '':
            return players[0]
        
        return None

    def new_game(self, players, board):
        """
        This function starts a new game.
        
        Parameters:
            players (list): The list of players.
            board (Board): The board object.
        
        Returns:
            The first player.
        """
        
        welcome_string = "Welcome players: {} is '{}', and {} is '{}'."
        
        print(welcome_string.format(
            players[0].color, self.get_player_game_piece(players[0].color),
            players[1].color, self.get_player_game_piece(players[1].color)))
        
        board.print_board()
        
        print('Your columns are 1 to 7, left to right.')
        
        first_player = None
        
        while first_player is None:
            first_player = self.first_player_selection_prompt(players)
        
        return first_player

    def end_game(self, winner, board):
        """
        This function ends the game. For a win or a draw, it prints the appropriate message.
        
        Parameters:
            winner (Player): The winner of the game.
            board (Board): The board object.
        """
        
        if winner is None:
            print('It was a draw!')
        else:
            print('Player {} won!'.format(winner.color))

    def print_board(self, the_board):
        """
        This function prints the connect 4 board. 
        """
        print()
        
        for row in range(the_board.height-1, -1, -1):
            
            print('|', end='')
            
            for column in range(the_board.width):
                
                space = the_board.board[column][row]
                
                if space == self.colors[0]:
                    print(self.get_player_game_piece(self.colors[0]), end='')
                
                if space == self.colors[1]:
                    print(self.get_player_game_piece(self.colors[1]), end='')
                
                if space is None:
                    print(' ', end='')
                
                print('|', end='')
            
            print()
        
        print('|' + '|'.join(str(col) for col in
              range(1, the_board.width+1)) + '|')
        print()

    def _exit(self):
            """
            This function exits the application with a message.
            """
            print('Exiting... Thanks for playing!')
            sys.exit(0)

    def concede(self, color):
        """
        This function concedes the game.
        
        Parameters:
            color (str): The color of the player.
        """
        print('Player {} has conceded.'.format(color))
        self._exit()

    def announce_move(self, color, move):
        """
        This function announces the move.
        
        Parameters:
            color (str): The color of the player.
            move (int): The move.
        """
        print('Player {} is placing game piece in column {}.'.format(color, move+1))

    def ask_for_player_move(self, color):
        """
        This function asks for the player move.
        
        Parameters:
            color (str): The color of the player.
        
        Returns:
            The player move.
        """
        
        try:
            input_ = input(self.ask_for_player_move_message.format(color))
        except KeyboardInterrupt:
            self._exit()
        
        print()
        
        if input_ == 'exit':
            self._exit()
        
        try:
            return int(input_)-1
        except:
            raise ValueError('Invalid move input.')