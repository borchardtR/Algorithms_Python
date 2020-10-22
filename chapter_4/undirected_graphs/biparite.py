# Title: biparite.py
# Author: Ryan Borchardt

# This implementation utilizes depth first search.

# This class extends the functionality of undirected graphs to be able to:
# 1. Determine if a graph is biparite.

# Note that:
# 1. If the graph is acyclic, it is automatically/guaranteed biparite / two-colorable.
# 2. If the graph has a cycle, it can still be biparite / two-colorable (if the cycles it contains have an even number of nodes, it can be biparite / two-colorable).

# Example:
# python biparite.py tinyG.txt ' '
#


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.undirected_graphs.graph_array_adjacencylists import Graph_Array_AdjacencyLists

class Biparite:
    def __init__(self, graph):
        self._marked_array = [False]*graph.V()
        self._biparite_array = [False]*graph.V()
        self._biparite = True
        # For each vertex, determine all of the other verticies that are connected to it.
        for i in range(graph.V()):
            if self._marked_array[i] != True:
                self._dfs(graph, i)
        
    def _dfs(self, graph, v):
        self._marked_array[v] = True

        adjacent_list = graph.adj[v] 
        for vertex in adjacent_list:
            if (self._marked_array[vertex]==True) and (self._biparite_array[vertex] == self._biparite_array[v]):
                self._biparite = False
            if self._marked_array[vertex] != True:
                self._biparite_array[vertex] = not self._biparite_array[v] 
                self._dfs(graph, vertex)
        

    
    def isBiparite(self):
        return self._biparite
        
        
def main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    graph = Graph_Array_AdjacencyLists(filename=filename, delimiter=delimiter)
    
    bp = Biparite(graph)
    
    print(bp._biparite_array)
    
    print(bp.isBiparite())

if __name__=="__main__":
    main()