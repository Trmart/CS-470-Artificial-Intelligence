# --------
# @file     main.py
# @author   Taylor Martin
# @date     May 2023
# @class    CS 470 Artificial Intelligence
#
# @brief    This file contains the environment class. Loads in the map from the file and stores it in a 2D array.
# --------------------

class Environment:

    """
    Enviornment Class 
    """


    def __init__(self):
        """
        Constructor
        """
        self.map_width = 0
        self.map_height = 0
        self.start = ()
        self.goal = ()
        self.map_size = 0
        self.map_file = "project1_map.txt"
        self.map = ()
        self.map = self.load_map(self.map_file)
        self.costs = { 'R': 1, 'f': 2, 'F': 4, 'h': 5, 'r': 7, 'M': 10, 'W': False}
        self.area_names = ["Road", "Field", "Forest", "Hills", "River", "Mountain", "Water"]

    def load_map(self, map_file):
        """
        Loads the map from the file into a 2D array
        """
        
        map = []

        with open(map_file, 'r') as f:
            map = f.readlines()
            f.close()

        self.map_size = tuple([int(i) for i in map[0].split()])
        self.start = tuple([int(i) for i in map[1].split()])
        self.goal = tuple([int(i) for i in map[2].split()])
        
        self.map_width = self.map_size[0]
        self.map_height = self.map_size[1]
        
        map = self.read_map(map[3:])
        
        return map
    
    def read_map(self, contents):
        """ Makes a tuple of tuple map from contents."""
        
        input_map = []
        
        for i in range(0, self.get_map_height()):
            input_map.append(tuple(list(contents[i])[:self.get_map_width()]))
        
        return tuple(input_map)
    
    def print_map(self):
        """
        Prints the map
        """
        for y in range(0,self.get_map_height()):
            for x in range(0,self.get_map_width()):
                if (x,y) == self.get_start():
                    print("S", end="")
                elif (x,y) == self.get_goal():
                    print("G", end="")
                else:
                    print(self.get_map()[y][x], end="")
            print()

    def get_map(self):
        """
        Returns the map
        """
        return self.map
    
    def get_map_width(self):
        """
        Returns the map width
        """
        return self.map_width
    
    def get_map_height(self):
        """
        Returns the map height
        """
        return self.map_height
    
    def get_start(self):
        """
        Returns the start position
        """
        return self.start
    
    def get_goal(self):
        """
        Returns the goal position
        """
        return self.goal
    
    def get_map_size(self):
        """
        Returns the map size
        """
        return self.map_size
    
    def get_costs(self):
        """
        Returns the costs
        """
        return self.costs
    
    def get_individual_costs(self, key):
        
        """
        Returns the individual costs
        """

        if key in self.costs:
            return self.costs[key]
        else:
            return None
    
    def print_environment(self):
        """
        Prints the environment
        """
        print("\n***************Environment***************")
        print("\nMap Width: ", self.map_width)
        print("Map Height: ", self.map_height)
        print("Start: ", self.start)
        print("Goal: ", self.goal)
        print("Map Size: ", self.map_size)
        print("\nMap: \n")
        self.print_map()
        self.print_costs()
    
    def print_costs(self):
        """
        Prints each element in costs and its name
        """
        
        print() 
        
        # fstring to print character, area, and cost with 4 spaces of padding
        print(f'{"Character:":15}{"Area:":10}{"Cost:":4}')
        
        i = 0
        for key, value in self.costs.items():
            print(f'{key:15}{self.area_names[i]:10}{value:4}')
            i += 1