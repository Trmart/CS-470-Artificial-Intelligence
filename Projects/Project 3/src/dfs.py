# --------------------
# @file     dfs.py
# @author   Taylor Martin
# @date     June 2023
# @class    CS 470 Artificial Intelligence
# @project  Project 3 - CSP
# @brief    This file contains the implementation of the DFS algorithm with two different heuristics. Least Constraining Value and Most Constrained Variable. To solve the map coloring CSP.
# --------------------



def select_most_constrained_variable(graph, colors):
    
    min_remaining_values = float('inf')
    most_constrained_variable = None
    
    for node in graph:
        
        if colors[node] is None:
            
            remaining_values = len(set(colors[neighbor] for neighbor in graph[node]))
            
            if remaining_values < min_remaining_values:
                min_remaining_values = remaining_values
                most_constrained_variable = node
    
    return most_constrained_variable


def dfs_most_constrained_variable(graph, colors):
    
    if all(colors[node] is not None for node in graph):
        return colors

    node = select_most_constrained_variable(graph, colors)
    
    for color in ['Red', 'Green', 'Blue']:
        
        if is_valid_color(node, color, graph, colors):
            
            colors[node] = color
            result = dfs_most_constrained_variable(graph, colors)
            
            if result is not None:
                return result
            
            colors[node] = None

    return None

def is_valid_color(node, color, graph, colors):
    
    for neighbor in graph[node]:
        
        if colors[neighbor] == color:
            
            return False
    
    return True

def select_fewest_remaining_values_variable(graph, colors):
    
    min_remaining_values = float('inf')
    fewest_remaining_values_variable = None
    
    for node in graph:
        
        if colors[node] is None:
            
            remaining_values = len(set(colors[neighbor] for neighbor in graph[node]))
            
            if remaining_values < min_remaining_values:
                
                min_remaining_values = remaining_values
                fewest_remaining_values_variable = node
    
    return fewest_remaining_values_variable

def dfs_fewest_remaining_values(graph, colors):
    
    if all(colors[node] is not None for node in graph):
        return colors

    node = select_fewest_remaining_values_variable(graph, colors)
    
    for color in ['Red', 'Green', 'Blue']:
        
        if is_valid_color(node, color, graph, colors):
            
            colors[node] = color
            
            result = dfs_fewest_remaining_values(graph, colors)
            
            if result is not None:
                return result
            
            colors[node] = None

    return None
