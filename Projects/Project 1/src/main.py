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

    
    # env = Environment()
    # env.print_environment()

    #for testing retrival of costs
    # test = env.get_individual_costs('f')
    # print("\n\n" + str(test))
    
    
    # env.save_map()

    agent = Agent()

    agent.env.print_environment()

    goal = agent.breadth_first_search()
    print("\n\nGoal: " + str(goal))

    path = agent.get_path()
    print("\n\nPath: " + str(path))
    print("\n\n Path Cost: " + str(agent.path_cost))
    print("\n\n Path Length: " + str(agent.path_length))
    
    print("\n\nExplored: ")
    agent.print_explored()
    
    print("\n\nPath: ")
    agent.print_path()

    

if __name__ == "__main__":
    """
    run main
    """
    main()