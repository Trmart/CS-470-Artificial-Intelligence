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
    def __init__(self, color, colors, interface):
        self.color = color
        self.colors = colors
        self.interface = interface
        
    def get_move(self, board):
        raise NotImplementedError("get_move not implemented")
    
class Human(Player):
    def __init__(self, color, colors, interface):
        super().__init__(color, colors, interface)
        
    def get_move(self, board = None):
        return self.interface.ask_move(self.color)

class Computer(Player):
    def __init__(self, color, colors, interface, difficulty = 1000):
        super().__init__(color, colors, interface)
        self.difficulty = difficulty
        
    def get_move(self, board):
        
        agent = Agent(board, self.colors)
        
        move, value = agent.min_max(self.color, self.difficulty)

        if move is None:
            self.interface.concede(self.color)
        
        self.interface.announce_move(self.color, move)
        return move