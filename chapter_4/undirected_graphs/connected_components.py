# Title: connected_components.py
# Author: Ryan Borchardt

# This implementation utilizes depth first search.

# This class extends the functionality of undirected graphs to be able to:
# 1. Determine if a path exists from a vertex to another vertex.
# 2. Determine which component a vertex is part of.
# 3. Determine the number of components in the graph.


# Example:
# python connected_components.py tinyG.txt ' '

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.undirected_graphs.graph_array_adjacencylists import Graph_Array_AdjacencyLists

class CC:
    def __init__(self, graph):
        self._marked_array = [False]*graph.V()
        self._id = [None]*graph.V()
        self._count = 0
        # For each vertex, determine all of the other verticies that are connected to it.
        for i in range(graph.V()):
            if self._marked_array[i] != True:
                self._dfs(graph, i)
                self._count += 1
        
    def _dfs(self, graph, v):
        self._marked_array[v] = True
        self._id[v] = self._count
        adjacent_list = graph.adj[v] 
        for vertex in adjacent_list:
            if self._marked_array[vertex] != True:
                self._dfs(graph, vertex)
        

    
    def connected(self, v, w):
        return self._id[v] == self._id[w]
        
    def count(self):
        return self._count
    
    def id(self, v):
        return self._id[v]
        
def main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    graph = Graph_Array_AdjacencyLists(filename=filename, delimiter=delimiter)
    
    cc = CC(graph)
    
    print(cc.count(), " components.")
    
    component_list = [list() for i in range(cc._count)]
    for i in range(graph.V()):
        component_list[cc.id(i)].append(i)
    
    for i in range(cc._count):
        string = "Component" + str(i) + ":"
        
        print("Component", i, ":")
        print(component_list[i])
    

if __name__=="__main__":
    main()