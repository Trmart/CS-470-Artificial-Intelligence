# For this option you will be implementing two or more versions of a CSP algorithm for a map coloring problem. Test data is given in CSPData.csv Download CSPData.csv as comma separated table. The upper right half of the table is filled in with 0's and 1's, where a 1 represents two "regions" that are neighboring and hence should have different colors and a 0 marks non-neighboring regions. (Note this data does not correspond to any actual map.)

# Abstractly, each of the variables X_1 through X_30 represent a different variable. If two variables are joined by a 1 in the table then they must be assigned different values.

# ## Project : Write a program to solve the map coloring problem.
# For this project try solving the problem with different numbers of colors: 2 colors, 3 colors, 4 colors, etc. until a successful solution is found.

# Test at least two different algorithms. A few options for the test algorithms include: local search, local search with min-conflicts, depth first search with 1 or more heuristics, and depth first search with forward checking.

# For each algorithm, record the number of steps required to find a solution. Also record the number of steps required to find a solution when the number of colors is increased by 1. For example, if the first solution is found with 3 colors, then record the number of steps required to find a solution with 4 colors. If the first solution is found with 4 colors, then record the number of steps required to find a solution with 5 colors.

class CSP:
    """"""