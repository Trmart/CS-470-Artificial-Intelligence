# --------------------
# @file     main.py
# @author   Taylor Martin
# @date     June 2023
# @class    CS 470 Artificial Intelligence
# @project  Project 3 - CSP
# @brief    This file contains the implementation of the main function to run the CSP algorithms.
# --------------------

from build_graph import build_graph
from dfs import dfs_most_constrained_variable , dfs_fewest_remaining_values
from local_search import min_conflicts
from time import time
from create_graphic import visualize_map
import networkx as nx
import matplotlib.pyplot as plt


def show_results(graph, solution, process_time):
    
    if solution is None:
        print("Failed to find a valid coloring.")
        print(f"Process time: {process_time} seconds")
        return
    else:
        print("Map coloring solution:")
        for node, color in solution.items():
            print(f"{node}: {color}")
        print(f"Process time: {process_time} seconds")

    nodes = []
    for node in graph:
        nodes.append(node)
    
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))

    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    # Visualize the graph with colored nodes
    visualize_map(graph, solution)


def main():
    filename = "CSPData.csv"
    graph = build_graph(filename)

    # Initialize colors
    colors = {node: None for node in graph}

    # Running the algorithm
    start_time = time()
    solution = dfs_most_constrained_variable(graph, colors)
    end_time = time()
    process_time = end_time - start_time
    show_results(graph, solution, process_time)

    colors = {node: None for node in graph}

    start_time = time()
    solution2 = dfs_fewest_remaining_values(graph, colors)
    end_time = time()
    process_time = end_time - start_time
    show_results(graph, solution2, process_time)

    start_time = time()
    solution3 = min_conflicts(graph, 1000, 10000)
    end_time = time()
    process_time = end_time - start_time
    show_results(graph, solution3, process_time)


if __name__ == "__main__":
    main()