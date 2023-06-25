# --------------------
# @file     create_graphic.py
# @author   Taylor Martin
# @date     June 2023
# @class    CS 470 Artificial Intelligence
# @project  Project 3 - CSP
# @brief    This file contains the implementation of a function to visualize the map coloring solution.
# --------------------

import networkx as nx
import matplotlib.pyplot as plt

def visualize_map(graph, node_colors, process_time):
    # Create a new figure
    plt.figure(figsize=(15, 15))

    # Create a layout for the nodes
    pos = nx.spring_layout(graph)

    # Draw the graph with node colors
    nx.draw_networkx(graph, pos, node_color=list(node_colors.values()))

    # Set axis labels and title
    plt.xlabel(f"Process time: {process_time} seconds")
    plt.title('Solved Map Coloring')

    # Show the plot
    plt.show()
