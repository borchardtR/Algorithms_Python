# Title: paths_dfs_recursive.py
# Author: Ryan Borchardt

# This implementation builds off of the code in dfs_recursive.py

# This class extends the functionality of undirected graphs to be able to:
# 1. Determine if a path exists from a vertex to another vertex (using the same dfs algorithm as in dfs_recursive.py and dfs_iterative.py).
# 2. Determine a path between two connected vertices.  


# Time complexity: Proportional to V + E (see explanation in dfs_recursive.py)
# Space complexity: Proportional to V

# the pathTo() method takes time proportional to the # of vertices on its path, which is a max of V.


# Example:
# python paths_dfs_recursive.py tinyCG.txt ' ' 0

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.undirected_graphs.graph_array_adjacencylists import Graph_Array_AdjacencyLists
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray

class Paths_dfs:
    def __init__(self, graph, s):
        self.path_array = [None]*graph.V()
        self.marked_array = [False]*graph.V()
        self.s = s
        
        self.dfs(graph, s)
    
    def dfs(self, graph, v):
        self.marked_array[v] = True
        bag_ll = graph.adj[v]
        # I implemented the bag_linkedlist data structure to be iterable (each iteration returns the item instance variable which in this case corresponds to the vertex).
        for neighbor_vertex in bag_ll:
            if self.marked_array[neighbor_vertex] == False:
                self.path_array[neighbor_vertex] = v
                self.dfs(graph, neighbor_vertex)
    
    def hasPathTo(self, v):
        return self.marked_array[v]
        
    def pathTo(self,v):
        if self.hasPathTo(v) == False: return None
        stack = Stack_ResizingArray()
        x = v
        while x is not None:
            stack.push(x)
            x = self.path_array[x]
        
        return stack
        
def main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    graph = Graph_Array_AdjacencyLists(filename=filename, delimiter=delimiter)
    s = int(sys.argv[3])
    
    paths = Paths_dfs(graph,s)
    
    print(paths.path_array)
    
    # the pathTo() method returns a stack object (which I have designed to be iterable) so for i in stack_object iterates through the items in each node of the bag
    for i in range(graph.V()):
        string = "0 to " + str(i) +": "
        for j in paths.pathTo(i):
            if j != i:
                string = string + str(j) + "->"
            else:
                string = string + str(j)
        print(string)

if __name__=="__main__":
    main()