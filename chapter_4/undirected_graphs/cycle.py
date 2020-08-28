# Title: cycle.py
# Author: Ryan Borchardt

# This implementation utilizes depth first search.

# This class extends the functionality of undirected graphs to be able to:
# 1. Determine if a graph contains a cycle or if it is acyclic.


# Example:
# python cycle.py tinyG.txt ' '
#


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.undirected_graphs.graph_array_adjacencylists import Graph_Array_AdjacencyLists

class Cycle:
    def __init__(self, graph):
        self._marked_array = [False]*graph.num_V()
        self._cycle = False
        # For each vertex, determine if there exists a cycle
        for i in range(graph.num_V()):
            self._marked_array = [False]*graph.num_V()
            self._dfs(graph, i, i)
        
    def _dfs(self, graph, v, prev_vertex):
        self._marked_array[v] = True

        adjacent_list = graph.adj[v] 
        for neighbor in adjacent_list:
            if self._marked_array[neighbor] != True:
                self._dfs(graph, neighbor, v)
            # If one of the neighbors (that was not the previous vertex) has already been marked, then we know there exists a cycle 
            elif (self._marked_array[neighbor] == True) and (neighbor != prev_vertex):
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