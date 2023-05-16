## CS470/570
## Artificial Intelligence
## Spring 2018
## Project #1 Pathfinding
## Due: Friday, Febuary 9th

## Background
Pathfinding is a search problem commonly encountered in computer strategy games. The goal in pathfinding is to find the least cost path between two points on a map. The map is divided into a discrete cells, usually squares or hexagons. Typically there is cost associated with moving into a cell, which depends on the terrain in a cell. E.g. moving into a forest square costs more than moving into a field. (You might consider why the cost is associated with moving into, rather than out of, a cell.)

In games pathfinding is typically an informed search; the agent knows approximately where the goal is and can calculate heuristics like the straight line distance from any point to the goal. In games the pathfinding environment is usually treated as fully observable. If parts of the map are unknown the agent may only plan a route to the edge of the observed region. If there are hidden obstacles, the agent typically picks a route ignoring them and must replan after finding them. (In some cases computer agents may be allowed to 'cheat' and observe more of the map than a human player would be allowed to.)


Although games are the most obvious application of pathfinding there are many other problems that require pathfinding. For example, determining the flow of water or oil between underground pools may require pathfinding with different types of soil and rock impeding the flow to a greater or lessor extent.


## Project: Test a number of different search strategies for pathfinding.

### Details: For this problem the map will use a rectangular grid. Agents will be able to move in four directions (up, down, left, right), but not diagonally.


Your program should be able to read a map file in the following format.
Width Height
StartX StartY
GoalX GoalY
map

Where the map is an array of characters. Width and Height define the width and height of the map. StartX, StartY, GoalX, 
and GoalY define the start and goal locations respectively. Note as a C++ programmer I have defined these positions 
