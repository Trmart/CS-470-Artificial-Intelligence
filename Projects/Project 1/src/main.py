# --------
# @file     main.py
# @author   Taylor Martin
# @date     May 2023
# @class    CS 470 Artificial Intelligence
#
# @brief    This file contains the main project function to run application
# --------------------

from agent import Agent

def main():
    """

    main function for Project 1: Pathfinding

    """


    agent = Agent()

    agent.env.print_environment()

    goal = agent.breadth_first_search()
    print("\n\nGoal: " + str(goal))

    path = agent.get_path()
    print("\n\nPath: " + str(path))

    print("\n\nNumber of Nodes Explored: " + str(agent.closed_list.__len__()))

    #path cost is correct
    print("\n\nPath Cost: " + str(agent.path_cost))

    # I think path length is correct. there are 27 nodes in the path list
    print("\n\nPath Length: " + str(agent.path_length))
    
    print("\n\nExplored: ")
    agent.print_explored()
    
    print("\n\nPath: ")
    agent.print_path()

    agent.save_path_to_file("BFS_path.txt")
    agent.save_explored_to_file("BFS_explored.txt")

    

if __name__ == "__main__":
    """
    run main
    """
    main()