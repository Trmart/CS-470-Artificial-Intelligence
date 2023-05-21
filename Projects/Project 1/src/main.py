# --------
# @file     main.py
# @author   Taylor Martin
# @date     May 2023
# @class    CS 470 Artificial Intelligence
#
# @brief    This file contains the main project function to run application
# --------------------

from environment import Environment
from agent import Agent

def main():
    """

    main function for Project 1: Pathfinding

    """

    
    env = Environment()
    env.print_environment()
    env.save_map()

if __name__ == "__main__":
    """
    run main
    """
    main()