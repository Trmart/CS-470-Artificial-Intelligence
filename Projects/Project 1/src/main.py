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


    # BFS ##
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


    ## Lowest Cost Search ##
    # agent = Agent()
    # agent.env.print_environment()
    
    agent.clear_lists()
    
    goal = agent.lowest_cost_search()
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

    agent.save_path_to_file("LCS_path.txt")
    agent.save_explored_to_file("LCS_explored.txt")

    ## A* ##
    
    agent.clear_lists()
    
    goal,cost = agent.a_star_search()
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

    agent.save_path_to_file("AStar_manhatten_path.txt")
    agent.save_explored_to_file("AStar_manhatten_explored.txt")

    ## A* with Heuristic 2 ##
    
    agent.clear_lists()
    
    goal,cost = agent.a_star_search("euclidean")
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

    agent.save_path_to_file("AStar_euclidian_path.txt")
    agent.save_explored_to_file("AStar_euclidian_explored.txt")

    

if __name__ == "__main__":
    """
    run main
    """
    main()