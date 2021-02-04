# Data Structures_ Ant_Optimization

This practical work consists in the implementation of an algorithm giving approximate solutions to the traveling salesman problem. This problem consists in finding the shortest path that visits each node of a graph exactly once and ends at the starting node. In this work, we focus on complete undirected graphs where the triangular inequality is respected.A voracious heuristic, called the nearest neighbor method, is to start at a random node and travel to the unvisited nearest neighbor until each node does. This heuristic will give di ff erent results depending on the starting point. Is L nn the cost of the minimum path given by this method applied to all possible starting points.
On average, this heuristic gives a path 25% longer than the optimal path, although it is technically possible that it gives us the solution
with the highest cost in the worst case. A superior approximate method proposed by Dorigo and Gambardella in 1996 uses an arti fi cial ant colony to find good solutions. This
model is inspired by the behavior of real ants, which can find the shortest paths between their nests and food sources by following the
pheromone trails left by other ants.

# Local track
τ (r, s) ← ( 1 - α) · τ (r, s) + α · τ 0

# Global track
τ (r, s) ← ( 1 - α) · τ (r, s) + α · Δ τ (r, s), where Δ τ (r, s) = 1/( Cost of the solution)

# Decision Making policy 
s = arg max{[ τ (r, u)] · [ η (r, u)] β} if q<q0

p = Σ[ τ (r, s)] · [ η (r, s)] β/ [ τ (r, u)] · [ η (r, u)] β if s belongs to M

# Language 
python ( shorttest path algorithm )
