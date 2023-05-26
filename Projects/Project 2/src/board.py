# --------
# @file     board.py
# @author   Taylor Martin
# @date     May 2023
# @class    CS 470 Artificial Intelligence
# @prof     Dr. Soule
# @project  Project 2: Connect 4
# @brief    This file contains the Board class.
# --------------------

#imports
from copy import deepcopy

"""Global Variables"""
MAX_ROWS = 6
MAX_COLS = 7

class Board():
    """
    This class represents the board for the game.
    
    Attributes:
        board: The board for the game.
    """

    def __init__(self):
        """
        The constructor for the board class.

        Parameters:
            board: The board for the game.
        """
        self.height = MAX_ROWS
        self.width = MAX_COLS
        self.board = [['_' for i in range(self.width)] for j in range(self.height)]

    def print_board(self):
        """
        This function prints the board.
        """
        for i in range(MAX_ROWS):
            for j in range(MAX_COLS):
                print(self.board[i][j], end=" ")
            print()
    
    def get_board(self):
        """
        This function returns the board.

        Returns:
            The board.
        """
        return deepcopy(self.board)
    
    def get_height(self):
        """
        This function returns the height of the board.

        Returns:
            The height of the board.
        """
        return self.height
    
    def get_width(self):
        """
        This function returns the width of the board.

        Returns:
            The width of the board.
        """
        return self.width
    
    def is_board_full(self):
        """
        This function checks if the board is full.

        Returns:
            True if the board is full, False otherwise.
        """
        for i in range(MAX_ROWS):
            for j in range(MAX_COLS):
                if self.board[i][j] == '_':
                    return False
        return True
    
    def is_win(self, color):
        """
        This function checks if there is a win.

        Returns:
            True if there is a win, False otherwise.
        """
        
        #horizontal
        for i in range(MAX_ROWS):
            for j in range(MAX_COLS-3):
                if self.board[i][j] == color and self.board[i][j+1] == color and self.board[i][j+2] == color and self.board[i][j+3] == color:
                    return True
        
        #vertical
        for i in range(MAX_ROWS-3):
            for j in range(MAX_COLS):
                if self.board[i][j] == color and self.board[i+1][j] == color and self.board[i+2][j] == color and self.board[i+3][j] == color:
                    return True
        
        #diagonal
        for i in range(MAX_ROWS-3):
            for j in range(MAX_COLS-3):
                if self.board[i][j] == color and self.board[i+1][j+1] == color and self.board[i+2][j+2] == color and self.board[i+3][j+3] == color:
                    return True
        
        return False