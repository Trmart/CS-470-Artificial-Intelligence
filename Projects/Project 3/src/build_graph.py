# --------------------
# @file     build_graph.py
# @author   Taylor Martin
# @date     June 2023
# @class    CS 470 Artificial Intelligence
# @project  Project 3 - CSP
# @brief    This file contains the implementation of a function to build a graph from a CSV file. In the format of X: [Y, Z, ...] where X is a variable and Y, Z, ... are the variables that X is constrained by.
# --------------------


import csv

def parse_csv_file(filename):
    variables = []
    constraints = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    num_variables = len(data[0])  # Assuming the number of variables is the same as the number of columns

    # Create variables
    for i in range(num_variables):
        variable = f'X{i+1}'
        variables.append(variable)

    # Create constraints
    for i in range(num_variables):
        for j in range(i + 1, num_variables):
            if data[i][j] == '1':
                constraint = (variables[i], variables[j])
                constraints.append(constraint)

    #combine variables and constraints into a single dictionary
    graph = {}
    for i in range(num_variables):
        graph[variables[i]] = constraints[i]
    

    return graph


def print_graph(graph):
    """
    Print a graph

    Args:   graph (dict): A dictionary of lists

    Returns:    None

    """
    for variable, neighbors in graph.items():
        print(f"{variable}: {neighbors}")


def build_graph(filename):
    """
    Build a graph from a CSV file. In this case, the CSV file is a map of regions that are neighbors. The graph is a dictionary of lists. The keys are the regions and the values are the neighbors of the region.

    Args:   filename (str): The name of the CSV file to parse

    Returns:    None

    Graph example:
    {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['A', 'B', 'C']
    }
    
    """
    graph = parse_csv_file(filename)
    print_graph(graph)
    return graph