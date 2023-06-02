# --------
# @file     agent.py
# @author   Taylor Martin
# @date     May 2023
# @class    CS 470 Artificial Intelligence
# @prof     Dr. Soule
# @project  Project 2: Connect 4
# @brief    This file contains the agent class.
# --------------------

import operator
import sys


class Agent():
    def __init__(self, board, colors):
        """
        Initializes the agent with the board and colors.
        
        Args:
            board (Board): The board object.
            colors (list): The list of colors.
        """
        self.board = board
        self.colors = colors
        self.max_player = None

    def get_other_player_color(self, color):
        """
        Returns the other color.

        Args:
            color (str): The color to check.
        """
        colors = list(self.colors)
        colors.remove(color)
        return colors[0]

    def min_max(self, color, difficulty):
        """
        Implements the min-max algorithm.

        Min Max Algorithm:
            1. Generate all possible moves for the current state.
            2. Evaluate each possible move.
            3. Return the best move.

        Args:
            color (str): The color to check.
            difficulty (int): The difficulty level.
        """
        player = color
        self.max_player = player
        opponent = self.get_other_player_color(color)
        depth = difficulty

        legal_moves = {}
        
        for column in range(self.board.width):
            
            if (self.board.is_valid_move(column, self.board.get_board()) is not None):
                
                state = self.simulate_move(self.board.get_board(),column, player)
                
                legal_moves[column] = -self.search(state, depth-1, opponent)
        
        return max(legal_moves.items(), key=operator.itemgetter(1))

    def simulate_move(self, state, column, color):
        """
       Simulates a move.

        Args:
            state (list): The state of the board.
            column (int): The column to make the move.
            color (str): The color to make the move.
        """
        row = self.board.is_valid_move(column, state)
        
        if row is None:
            raise ValueError("Invalid move")
        
        state[column][row] = color
        
        return state

    def search(self, state, depth, player, alpha=-sys.maxsize, beta=sys.maxsize):
        """
        Searches the state space. This is a recursive function. It also implements alpha-beta pruning to improve the performance of the algorithm.

        Args:
            state (list): The state of the board.
            depth (int): The depth to search.
            player (str): The player to search.
            alpha (int): The alpha value.
            beta (int): The beta value.
        """
        opp = self.get_other_player_color(player)
        
        legal_moves = []
        
        for column in range(self.board.width):
            if self.board.is_valid_move(column, state) is not None:
                legal_moves.append(self.simulate_move(state, column, player))

        if depth == 0 or legal_moves is None or self.game_over(state):
            return self.value(state, player)

        if player == self.max_player:
            
            for move in legal_moves:
                
                alpha = max(alpha, -self.search(move, depth-1, opp, alpha, beta))
                
                if beta <= alpha:
                    break
            
            return alpha
        
        else:
            for move in legal_moves:
                
                beta = min(beta, -self.search(move, depth-1, opp, alpha, beta))
                
                if beta <= alpha:
                    break
            
            return beta

    def check_for_streak(self, state, color, streak):
        """
        Checks for a streak of a given length. This function checks for vertical, horizontal, and diagonal streaks.

        Args:
            state (list): The state of the board.
            color (str): The color to check.
            streak (int): The length of the streak.
        """
        streaks = 0
        
        for col in range(self.board.get_width()):
            for row in range(self.board.get_height()):
                if state[col][row] == color:
                    streaks += self.vertical_streak(col, row, state, streak)
                    streaks += self.horizontal_streak(col, row, state, streak)
                    streaks += self.diagonal_streak(col, row, state, streak)
        return streaks

    def game_over(self, state):
        """
        Checks if the game is over.
        
        Args:
            state (list): The state of the board.
        """
        return (self.check_for_streak(state, self.colors[0], 4) >= 1 or
                self.check_for_streak(state, self.colors[1], 4) >= 1)

    def value(self, state, color):
        """
        Returns the value of the state.
        
        Args:
            state (list): The state of the board.
            color (str): The color to check.
        """
        player = color
        
        opponent = self.get_other_player_color(player)
        
        fours = self.check_for_streak(state, player, 4)
        
        threes = self.check_for_streak(state, player, 3)
        
        twos = self.check_for_streak(state, player, 2)
        
        losses = self.check_for_streak(state, opponent, 4)
        
        if losses > 0:
            return -sys.maxsize
        
        else:
            return (fours*16 + threes*4 + twos*2)

    def vertical_streak(self, icol, irow, state, streak):
        """
        Checks for a vertical streak.
        
        Args:
            icol (int): The column to check.
            irow (int): The row to check.
            state (list): The state of the board.
            streak (int): The length of the streak.
        """
        count = 0
        
        for row in range(irow, self.board.height):
            if state[icol][row] == state[icol][irow]:
                count += 1
            else:
                break
        
        for row in range(irow, -1, -1):
            if state[icol][row] == state[icol][irow]:
                count += 1
            else:
                break
        
        return int(count >= streak)

    def horizontal_streak(self, icol, irow, state, streak):
        """
        Checks for a horizontal streak.
        
        Args:
            icol (int): The column to check.
            irow (int): The row to check.
            state (list): The state of the board.
            streak (int): The length of the streak.
        """
        count = 0
        
        for col in range(icol, self.board.width):
            if state[col][irow] == state[icol][irow]:
                count += 1
            else:
                break
        
        for col in range(icol, -1, -1):
            if state[col][irow] == state[icol][irow]:
                count += 1
            else:
                break
        
        return int(count >= streak)

    def diagonal_streak(self, icol, irow, state, streak):
        """
        Checks for a diagonal streak. This function checks for diagonals with positive and negative slopes.
        
        Args:
            icol (int): The column to check.
            irow (int): The row to check.
            state (list): The state of the board.
            streak (int): The length of the streak.
        """
        total = 0
        
        # check for diagonals with positive slope
        count = 0
        col = icol
        
        for row in range(irow, self.board.height):
            
            if col >= self.board.width or col < 0:
                break
            
            if state[col][row] == state[icol][irow]:
                count += 1
            
            else:
                break
            
            col += 1  # increment column when row is incremented
        
        total += int(count >= streak)

        # check for diagonals with negative slope
        
        count = 0
        
        col = icol
        
        for row in range(irow, -1, -1):
            
            if col >= self.board.width or col < 0:
                break
            
            elif state[col][row] == state[icol][irow]:
                count += 1
            
            else:
                break
            
            col += 1  # increment column when row is incremented
        
        total += int(count >= streak)

        return total