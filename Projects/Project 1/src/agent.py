# --------
# @file     agent.py
# @author   Taylor Martin
# @date     May 2023
# @class    CS 470 Artificial Intelligence
#
# @brief    This file contains the agent class. For traversing the map generated by the environment class. Utilizes various AI pathfinding algorithms for traversal.
# --------------------

from environment import Environment
import math

class Agent:
    
    """
    Agent Class 
    """

    def __init__(self):
        """
        Constructor
        """
        self.env = Environment()
        self.path = {}
        self.path_cost = 0
        self.path_length = 0
        self.closed_list = set()
        self.open_list = []

    def clear_lists(self):
        """
        Clear lists
        """
        self.path = {}
        self.path_cost = 0
        self.path_length = 0
        self.closed_list = set()
        self.open_list = []
    
    def is_goal(self, state):
        """
        Check if state is goal
        """
        if state == self.env.get_goal():
            return True
        else:
            return False
    
    def is_not_explored(self, state):
        """
        Check if state is not explored
        """
        return (state not in self.open_list and state not in self.closed_list)
        
    def record_agent_path(self, parent, child):
        """
        Record agent path
        """
        self.path[child] = parent

    def get_path(self):
        """
        Get path
        """
        path = [self.env.get_goal()]
        
        while path[-1] != self.env.get_start():
            path.append(self.path[path[-1]])
        path.reverse()
        
        return tuple(path)
    
    def print_path(self):
        """
        Print path
        """
        for y in range(0,self.env.get_map_height()):
            for x in range(0,self.env.get_map_width()):
                if (x,y) == self.env.get_start():
                    print("S", end="")
                elif (x,y) == self.env.get_goal():
                    print("G", end="")
                elif (x,y) in self.get_path():
                    print("*", end="")
                elif (x,y) in self.open_list:
                    print("#", end="")
                else:
                    print(self.env.get_map()[y][x], end="")
            print()

    def print_explored(self):
        """
        Print path
        """
        for y in range(0,self.env.get_map_height()):
            for x in range(0,self.env.get_map_width()):
                if (x,y) == self.env.get_start():
                    print("S", end="")
                elif (x,y) == self.env.get_goal():
                    print("G", end="")
                elif (x,y) in self.get_path():
                    print("*", end="")
                elif (x,y) in self.closed_list:
                    print("$", end="")
                else:
                    print(self.env.get_map()[y][x], end="")
            print()
    
    def save_path_to_file(self, output_file):
        """
        Save the agent path to a file.
        """

        with open(output_file, 'w') as file:
            file.write("*******************Agent Path***********************\n")
            file.write("Map Size: " + str(self.env.get_map_size()) + "\n")
            file.write("Map Width: " + str(self.env.get_map_width()) + "\n" + "Map Hight: " + str(self.env.get_map_height()) + "\n")
            file.write("Starting Point: " + str(self.env.get_start()) + "\n")
            file.write("Goal Point: " + str(self.env.get_goal()) + "\n")
            
            file.write(f'\nState Costs:\n\n')
            file.write(f'{"Character:":15}{"Area:":10}{"Cost:":4}\n')
        
            i = 0
            for key, value in self.env.get_costs().items():
                file.write(f'{key:15}{self.env.area_names[i]:10}{value:4}\n')
                i += 1

            file.write("\n\nAgent Symbol Legend:\n")
            file.write("S = Start\n")
            file.write("G = Goal\n")
            file.write("* = Path\n")
            file.write("# = Open List\n")
            
            path = self.get_path()
            file.write("\n\nAgent Path: " + str(path))

            file.write("\n\nNumber of Nodes Explored: " + str(self.closed_list.__len__()))

            #path cost is correct
            file.write("\n\nPath Cost: " + str(self.path_cost))

            # I think path length is correct. there are 27 nodes in the path list
            file.write("\n\nPath Length: " + str(self.path_length))
            file.write("\n\nPath: \n")
            

            for y in range(0,self.env.get_map_height()):
                for x in range(0,self.env.get_map_width()):
                    if (x,y) == self.env.get_start():
                        file.write("S")
                    elif (x,y) == self.env.get_goal():
                        file.write("G")
                    elif (x,y) in self.get_path():
                        file.write("*")
                    elif (x,y) in self.open_list:
                        file.write("#")
                    else:
                        file.write(self.env.get_map()[y][x])
                file.write('\n')

            
            file.close()
    
    def save_explored_to_file(self, output_file):
        """
        save the explored path to file
        """

        with open(output_file, 'w') as file:
            
            file.write("*******************Agent Nodes Explored***********************\n")
            file.write("Map Size: " + str(self.env.get_map_size()) + "\n")
            file.write("Map Width: " + str(self.env.get_map_width()) + "\n" + "Map Hight: " + str(self.env.get_map_height()) + "\n")
            file.write("Starting Point: " + str(self.env.get_start()) + "\n")
            file.write("Goal Point: " + str(self.env.get_goal()) + "\n")
            
            file.write(f'\nState Costs:\n\n')
            file.write(f'{"Character:":15}{"Area:":10}{"Cost:":4}\n')
        
            i = 0
            for key, value in self.env.get_costs().items():
                file.write(f'{key:15}{self.env.area_names[i]:10}{value:4}\n')
                i += 1
            
            file.write("\n\nAgent Symbol Legend:\n")
            file.write("S = Start\n")
            file.write("G = Goal\n")
            file.write("* = Path\n")
            file.write("$ = Closed List\n")

            path = self.get_path()
            file.write("\n\nAgent Path: " + str(path))

            file.write("\n\nNumber of Nodes Explored: " + str(self.closed_list.__len__()))

            #path cost is correct
            file.write("\n\nPath Cost: " + str(self.path_cost))

            # I think path length is correct. there are 27 nodes in the path list
            file.write("\n\nPath Length: " + str(self.path_length))
            
            file.write("\n\nPath: \n")
            for y in range(0,self.env.get_map_height()):
                for x in range(0,self.env.get_map_width()):
                    if (x,y) == self.env.get_start():
                        file.write("S")
                    elif (x,y) == self.env.get_goal():
                        file.write("G")
                    elif (x,y) in self.get_path():
                        file.write("*")
                    elif (x,y) in self.closed_list:
                        file.write("$")
                    else:
                        file.write(self.env.get_map()[y][x])
                file.write('\n')
            
        file.close()
    
    def get_state_cost(self, state):
        """
        Get state cost
        """
        x,y = state
        return self.env.get_costs()[self.env.get_map()[y][x]]
    
    def add_to_openlist(self, state, cost = None):
        """
        Add to open list
        """
        if cost is not None:
            self.open_list.append([state, cost])
        else:
            self.open_list.append(state)

    def add_to_closedlist(self, state):
        """
        Add to closed list
        """
        self.closed_list.add(state)
    
    def remove_from_openlist(self, index):
        """
        Remove from open list
        """
        self.open_list.pop(self.open_list.index(index))
    
    def remove_from_closedlist(self, state):
        """
        Remove from closed list
        """
        try:
            self.closed_list.remove(state)
        except KeyError:
            pass
    
    def get_next_open_list_head(self):
        """
        Get next open list head
        """
        return self.open_list.pop(0)
    
    def get_next_open_list_tail(self):
        """
        Get next open list tail
        """
        return self.open_list.pop()
    
    def is_valid_state(self, state):
        """
        Check if state is valid
        """ 
        x, y = state
        # print("x: " + str(x) + " y: " + str(y))
        
        if (x >= 0 and 
            y >= 0 and 
            x < self.env.get_map_width() and 
            y < self.env.get_map_height() and 
            self.env.get_map()[y][x] != 'W'):
            return True
        else:
            return False
    
    def is_in_openlist(self, state):
        for i in self.open_list:
            if state == i[0]:
                return True
        return False
    
    def fringe_higher(self, state, cost, append=True):
        for i in self.open_list:
            if state == i[0]:
                if i[1] >= cost:
                    self.remove_from_openlist(i)
                    if append:
                        self.add_to_openlist(state, cost)
                    return True
                else:
                    return False
                
    def expand_node(self, state, sort = False, reverse = False):
        """
        Expand node
        """
        result = []

        x, y = state

        neighbors = (
                        (x, y-1),
                        (x, y+1),
                        (x+1, y),
                        (x-1, y)
                    )
        
        for neighbor in neighbors:
            if self.is_valid_state(neighbor):
                result.append(neighbor)
        
            if sort:
                result.sort(key=lambda state: self.get_state_cost(state))
            if reverse:
                result.reverse()

        return result

    def euclidean_distance(self, state):
        """
        Euclidean distance / Straight line distance
        """
        x1, y1 = state
        x2, y2 = self.env.get_goal()
        
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def manhattan_distance(self, state):
        """
        Manhattan distance / Taxicab distance
        """
        x1, y1 = state
        x2, y2 = self.env.get_goal()
        
        return (abs(x1 - x2) + abs(y1 - y2))

    def breadth_first_search(self):
        """
        Breadth First Search
        """
        self.add_to_openlist(self.env.get_start())
        # print(self.open_list)
        
        while self.open_list:
            
            parent = self.get_next_open_list_head()
            # print(parent)
            
            if self.is_goal(parent):
                for state in self.get_path():
                    self.path_cost += self.get_state_cost(state)
                self.path_length = len(self.get_path())
                return parent
            
            for child in self.expand_node(parent):
                if self.is_not_explored(child):
                    self.record_agent_path(parent, child)
                    self.add_to_openlist(child)
            self.add_to_closedlist(parent)
        
        return None

    def lowest_cost_search(self, heuristic = "manhattan"):
        """
        Lowest Cost Search, aka Uniform Cost Search
        """

        node , cost = self.a_star_search(heuristic)
        return node
    
    def greedy_best_first_search(self):

        """
        Greedy Best First Search
        """
    
    
    def a_star_search(self, heuristic = "manhattan"):
        """
        A* Search
        """
        self.add_to_openlist(self.env.get_start(),0)

        while self.open_list:
            parent, cost = self.get_next_open_list_head()

            if self.is_goal(parent):
                for state in self.get_path():
                    self.path_cost += self.get_state_cost(state)
                self.path_length = len(self.get_path())
                return parent,cost
            
            self.add_to_closedlist(parent)

            for child in self.expand_node(parent):
                
                if heuristic == "manhattan":
                    child_cost = cost + self.get_state_cost(child) + self.manhattan_distance(child)
                if heuristic == "euclidean":
                    child_cost = cost + self.get_state_cost(child) + self.euclidean_distance(child)

                if child not in self.closed_list:
                    if not self.is_in_openlist(child):
                        self.record_agent_path(parent, child)
                        self.add_to_openlist(child, child_cost)
                elif self.fringe_higher(child, child_cost):
                    self.record_agent_path(parent, child)
                    self.remove_from_closedlist(child)
            
            ## sort openlist is ascending order of state costs
            self.open_list.sort(key=lambda x: x[1])
        
        return None
