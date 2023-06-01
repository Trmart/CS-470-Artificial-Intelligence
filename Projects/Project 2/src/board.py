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

    def __init__(self,interface = None):
        """
        The constructor for the board class.

        Parameters:
            board: The board for the game.
        """
        self.height = MAX_ROWS
        self.width = MAX_COLS
        self.board = []
        for _ in range(self.width):
            self.board.append([None] * self.height)
        self.interface = interface

    # def print_board(self):
    #     """
    #     This function prints the board.
    #     """
    #     for i in range(MAX_ROWS):
    #         for j in range(MAX_COLS):
    #             if(self.board[i][j] == 'B'):
    #                 # self.interface.draw_red_circle(j,i)
    #                 blue = "\u001b[34m"
    #                 pass
    #             elif(self.board[i][j] == 'G'):
    #                 green = "\u001b[32m"
    #                 # self.interface.draw_yellow_circle(j,i)
    #                 pass
    #             else:
    #                 # self.interface.draw_white_circle(j,i)
    #                 green = "\u001b[32m"
    #                 # print("_", end=" ")
    #                 print("_", end=" | ")
    #             # print(self.board[i][j], end=" ")
    #         print("\n----------------------------")

    def print_board(self):
        self.interface.print_board(self)
    
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
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                if self.board[i][j] == None:
                    return False
        return True
    
    def is_valid_move(self,move, board=None):
        """Returns True if the move is valid, False otherwise."""
        
        if board is None:
            board = self.get_board()
        if move < self.width:
            row = self.get_next_empty_row(move, board)
            if row is None:
                return None
            if board[move][row] is None:
                return row
        else:
            return None
        
    def get_next_empty_row(self, move, board):
        """Returns the next empty row in the column."""
        for row, value in enumerate(board[move]):
            if value is None:
                return row
        return None
    
    def make_move(self, move, color):
        """Makes the move on the board."""
        
        row = self.is_valid_move(move)
        
        if  row is not None:
            self.board[move][row] = color
            return (move,row)
        
        raise Exception("Invalid move: column is full.")
    
    def is_win(self, color):
        """
        This function checks if there is a win.

        Returns:
            True if there is a win, False otherwise.
        """
        
        #horizontal
        for i in range(self.get_width()-3):
            for j in range(self.get_height()):
                if self.board[i][j] == color and self.board[i][j+1] == color and self.board[i][j+2] == color and self.board[i][j+3] == color:
                    return True
        
        #vertical
        for i in range(self.get_width()):
            for j in range(self.get_height()-3):
                if self.board[i][j] == color and self.board[i+1][j] == color and self.board[i+2][j] == color and self.board[i+3][j] == color:
                    return True
        
        #diagonal
        for i in range(self.get_width()-3):
            for j in range(self.get_height()-3):
                if self.board[i][j] == color and self.board[i+1][j+1] == color and self.board[i+2][j+2] == color and self.board[i+3][j+3] == color:
                    return True
                
        #diagonal
        for i in range(self.get_width()-3):
            for j in range(3, self.get_height()):
                if self.board[i][j] == color and self.board[i+1][j-1] == color and self.board[i+2][j-2] == color and self.board[i+3][j-3] == color:
                    return True
        
        return False