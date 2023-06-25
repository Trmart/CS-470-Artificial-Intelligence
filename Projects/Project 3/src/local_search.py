# --------------------
# @file     local_search.py
# @author   Taylor Martin
# @date     June 2023
# @class    CS 470 Artificial Intelligence
# @project  Project 3 - CSP
# @brief    This file contains the implementation of a local search algorithm with the min conflict heuristic. To solve the map coloring CSP.
# --------------------


import random

def generate_initial_state(graph, num_colors):
    
    variables = list(graph.keys())
    
    state = {}
    
    for variable in variables:
        state[variable] = random.randint(1, num_colors)
    
    return state

def count_conflicts(variable, color, state, graph):
    
    conflicts = 0
    neighbors = graph[variable]
    
    for neighbor in neighbors:
        
        if state[neighbor] == color:
            conflicts += 1
    
    return conflicts

def min_conflicts(graph, num_colors, max_steps):
    
    state = generate_initial_state(graph, num_colors)
    
    for _ in range(max_steps):
        
        conflicted_variables = [variable for variable in graph if count_conflicts(variable, state[variable], state, graph) > 0]
        
        if len(conflicted_variables) == 0:
            return state
        
        variable = random.choice(conflicted_variables)
        min_conflicts = float('inf')
        min_color = None
        
        for color in range(1, num_colors + 1):
            
            conflicts = count_conflicts(variable, color, state, graph)
            
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                min_color = color
        
        state[variable] = min_color
    
    return None
