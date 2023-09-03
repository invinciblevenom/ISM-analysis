# ISM-analysis

An Interpretive Structural Modelling approach for Building information modelling adoption.

## Class Graph:

This class represents a directed graph and is used to calculate the transitive closure of the given graph using the Floyd-Warshall algorithm.
The transitive_closure method computes the transitive closure of the graph using a nested loop structure and returns the reachability matrix.

## Functions:

print_final_reachability(initial, final): This function prints the final reachability matrix, indicating whether each pair of nodes has a reachability path between them.
level_partioning(final): This function generates a common matrix that shows the direct reachability relationships for each node.
stop_crit(level): This function checks whether the given level array contains any zero, which is used as a stopping criterion in a loop.
x_and_y(final): This function calculates the driving power and dependence power for each node in the graph based on the reachability matrix.
find_level(intersection_set, common_mat): This function calculates the levels of variables (risks) based on the intersection of reachability sets.

## Plotting Function:

The plot_it(driving_power, dependence_power) function creates a scatter plot of dependence power vs. driving power for each node (risk). It uses Matplotlib to visualize the data points and relationships among variables.

## Main Execution:

The code prompts the user for the dimension of the reachability matrix and the name of the input file.
It loads the input file data into a matrix and then calculates the transitive closure of the graph using the Graph class.
The driving power and dependence power for each node are calculated using the x_and_y function.
The common matrix and intersection set are computed for level partitioning.
The levels of variables are calculated using the find_level function.
The plot_it function is called to visualize the relationships among variables using a scatter plot.
Finally, a PrettyTable is created to display the levels of each variable in tabular form.

### The data in inp.txt has been taken from a research paper and used here only for reference.
