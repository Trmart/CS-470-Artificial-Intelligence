# --------
# @file     game.py
# @author   Taylor Martin
# @date     May 2023
# @class    CS 470 Artificial Intelligence
# @prof     Dr. Soule
# @project  Project 2: Connect 4
# @brief    This file contains the game class.
# --------------------


# Imports
from random import choice

from board import Board
from player import Human, Computer


class Game:
    """
    This class represents a game.

    Attributes:
        interface (Interface): The interface.
        playing (bool): Whether or not the game is playing.
        winner (Player): The winner of the game.
        colors (list): The list of colors.
        board (Board): The board object.
        players (list): The list of players.
    """

    def __init__(self, interface, colors, player_types):

        """
        The constructor for the game class. It initializes the game.

        Parameters:
            interface (Interface): The interface.
            colors (list): The list of colors.
            player_types (list): The list of player types.
        """
        
        self.interface = interface
        self.playing = True
        self.winner = None
        self.colors = colors
        self.board = Board(self.interface)
        self.players = []
        
        for player in player_types:
            self.players.append(
                eval(player)(self.get_player_color(), self.colors, self.interface))

    def get_player_color(self):
        """
        This function gets the color for the player.
        
        Returns:
            The color for the player.
        """
        
        if not self.players:
            return choice(self.colors)
        
        else:
            colors = list(self.colors)
            colors.remove(self.players[0].color)
            return colors[0]

    def player_turn(self, player, board):
        """
        This function gets the move for the player.
        
        Parameters:
            player (Player): The player.
            board (Board): The board object.
        """
        try:
            column = player.get_move(board)
            move = self.board.make_move(column, player.color)
        except ValueError:
            return None
        return move

    def assign_player_ordering(self, player):
        """
        This function assigns the player ordering.
        
        Parameters:
            player (Player): The player.
        """
        if self.players.index(player) != 0:
            self.players.reverse()

    def play(self):
        """
        This function plays the game.
        
        Returns:
            The winner of the game. Or None if there is no winner (tie).
        """
        self.assign_player_ordering(self.interface.new_game(self.players, self.board))
        
        while self.playing:
            
            for player in self.players:
                move = None
                
                while move is None:
                    move = self.player_turn(player, self.board)
                self.board.print_board()
                
                if self.board.is_win(player.color):
                    self.winner = player
                    self.playing = False
                    break
                
                if self.board.is_board_full():
                    self.winner = None
                    self.playing = False
                    break
        
        self.interface.end_game(self.winner, self.board)