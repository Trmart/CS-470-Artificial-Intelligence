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
        self.start = []
        self.goal = []
        self.map_size = 0
        self.map_file = "project1_map.txt"
        self.output_file = "project1_output.txt"
        self.map = []
        self.map = self.load_map(self.map_file)
        self.costs = { 'R': 1, 'f': 2, 'F': 4, 'h': 5, 'r': 7, 'M': 10, 'W': 100}
        self.area_names = ["Road", "Field", "Forest", "Hills", "River", "Mountain", "Water"]

    def load_map(self, map_file):
        """
        Loads the map from the file into a 2D array
        """
        
        map = []
        
        with open(map_file) as file:
            for line in file:
                map.append(line.split())
        
        self.map_width = int(map[0][0])
        
        self.map_height = int(map[0][1])
        
        self.start = [int(map[1][0]), int(map[1][1])]
        
        self.goal = [int(map[2][0]), int(map[2][1])]
        
        self.map_size = self.map_width * self.map_height
        
        map = map[3:]
        
        return map
    
    def save_map(self):
        """
        Save the map to a file
        """
        with open(self.output_file, 'w') as file:
            
            file.write(str(self.map_width) + " " + str(self.map_height) + "\n")
            file.write(str(self.start[0]) + " " + str(self.start[1]) + "\n")
            file.write(str(self.goal[0]) + " " + str(self.goal[1]) + "\n")
            file.write(str(self.map_size) + "\n")
            
            for row in self.map:
                for col in row:
                    file.write(col + " ")
                file.write("\n")
            file.write(str())

            file.write(f'{"Character:":15}{"Area:":10}{"Cost:":4}')
        
            i = 0
            for key, value in self.costs.items():
                file.write(f'{key:15}{self.area_names[i]:10}{value:4}')
                i += 1
            
            file.close()
    
    def print_map(self):
        """
        Prints the map
        """
        for row in self.map:
            for col in row:
                print(col, end=" ")
            print()
    
    
    def print_map_path(self, path):
        """
        Prints the map with the path
        """
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if [i, j] in path:
                    print("X", end=" ")
                else:
                    print(self.map[i][j], end=" ")
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