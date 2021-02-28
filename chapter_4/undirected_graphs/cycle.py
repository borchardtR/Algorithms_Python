# Title: cycle.py
# Author: Ryan Borchardt

# This implementation utilizes depth first search. dfs automatically stores the previous vertex as v.

# This class extends the functionality of undirected graphs to be able to:
# 1. Determine if a graph contains a cycle or if it is acyclic.


# Example:
# python cycle.py tinyG.txt ' '
#


import sys
from chapter_4.undirected_graphs.graph_array_adjacencylists import Graph_Array_AdjacencyLists

class Cycle:
    def __init__(self, graph):
        self._marked_array = [False]*graph.V()
        self._cycle = False
        # For each component in the graph, determine if there exists a cycle
        for i in range(graph.V()):
             if not self._marked_array[i]:
                self._dfs(graph, i, i)
        
    def _dfs(self, graph, v, calling_vert):
        self._marked_array[v] = True

        adjacent_list = graph.adj[v] 
        for neighbor in adjacent_list:
            if not self._marked_array[neighbor]:
                self._dfs(graph, neighbor, v)
            # If neighbor has already been marked and it is NOT the calling vertex, we know we have found a cycle in the graph:
            elif neighbor != calling_vert:
                self._cycle = True
        

    
    def hasCycle(self):
        return self._cycle
        
        
def main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    graph = Graph_Array_AdjacencyLists(filename=filename, delimiter=delimiter)
    
    cyc = Cycle(graph)
    
    print('cyclic:', cyc.hasCycle())

if __name__=="__main__":
    main()