# --------
# @file     player.py
# @author   Taylor Martin
# @date     May 2023
# @class    CS 470 Artificial Intelligence
# @prof     Dr. Soule
# @project  Project 2: Connect 4
# @brief    This file contains the player class.
# --------------------

# Imports
from agent import Agent

class Player:
    """
    This class represents a player.
    
    Attributes:
        color (str): The color of the player.
        colors (list): The list of colors.
        interface (Interface): The interface.
    """
    
    def __init__(self, color, colors, interface):
        """
        The constructor for the player class. 

        Parameters:
            color (str): The color of the player.
            colors (list): The list of colors.
            interface (Interface): The interface.
        """
        self.color = color
        self.colors = colors
        self.interface = interface
        
    def get_move(self, board):
        """
        This function gets the move for the player. It must be overridden by the child class.
        """
        raise NotImplementedError("get_move not implemented")
    
class Human(Player):
    """
    This class represents a human player.
    
    Attributes:
        color (str): The color of the player.
        colors (list): The list of colors.
        interface (Interface): The interface.
    """
    def __init__(self, color, colors, interface):
        """
        The constructor for the human class. It calls the parent constructor.
        """
        super().__init__(color, colors, interface)
        
    def get_move(self, board = None):
        return self.interface.ask_for_player_move(self.color)

class Computer(Player):
    """"
    This class represents a computer player.
    """
    def __init__(self, color, colors, interface, difficulty = 10000):
        """"
        The constructor for the computer class. It calls the parent constructor.
        
        Parameters:
            difficulty (int): The difficulty level.
        """
        super().__init__(color, colors, interface)
        self.difficulty = difficulty
        
    def get_move(self, board):
        """
        This function gets the move for the computer.
        
        Parameters:
            board (Board): The board object.
        """
        agent = Agent(board, self.colors)
        
        move, value = agent.min_max(self.color, self.difficulty)

        if move is None:
            self.interface.concede(self.color)
        
        self.interface.announce_move(self.color, move)
        return move