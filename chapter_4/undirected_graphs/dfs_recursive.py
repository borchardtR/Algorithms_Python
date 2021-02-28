# Title: dfs_recursive.py
# Author: Ryan Borchardt

"""
This class extends the functionality of undirected graphs to be able to:
1. Determine if a path exists from a vertex to another vertex.
2. Determine the number of vertices a vertex is connected to.

I am implementing the depth first search algorithm.
This particular implementation of depth first search is for undirected, unweighted graphs. 

This class can be directly used to determine for a given vertex (s):
    1. If a vertex, v, is connected to s.
    2. The # of vertices connected to s.

# Note that as I see it there are atleast 8+ main ways to implement the DFS algorithm:
    1. DFS as a separate data structure
    2. DFS as a separate function
    3. DFS as a few instance methods within the Graph data structure
    4. DFS as a few instance variables + a few instance methods within the Graph data structure
    Each of the above ways can be implemented recursively or iteratively
    There are different tradeoffs to all of the ways I have listed. The best choice will depend on what you want to do with it.
        Example 1: You will frequently be checking whether a given vertex is connected to a source vertex.
            You should implement DFS as a separate data structure or as a few instance variables within the graph data structure (this way the underling DFS algorithm only needs to be run once for a given graph and source vertex, no matter how many times count() or marked() is called.
        Example 2: You don't want your API interface to be too wide
            You should implement DFS as a separate data strucutre or as a separate function.
        Etc.
    
I have decided to implement depth first search using the same way that it is done in Sedgewick and Wayne's Algorithms (DFS as a separate data structure implemented recursively).
I implemented depth first seach as a separate data structure implemented iteratively in dfs_iterative.py
    I did this to explicitly show the usage of a stack to implement dfs (the recursive version uses the call stack).

Time complexity: Proportional to V + E
Space complexity: Proportional to V (the marked array has length V)

It takes time proportional to V+E b/c:
    1. the line 'self.marked_array[v] =True' is executed V times
    2. the line 'if self.marked_array[neighbor_vertex] == True' is evaluated 2*E times (E times it is True, E times it is False)


After the data structure has been instantiated, marked() and count() take constant time.

"""

# Example:
# python dfs_recursive.py tinyCG.txt ' ' 0 2 5

import sys
from chapter_4.undirected_graphs.graph_array_adjacencylists import Graph_Array_AdjacencyLists


class DFS_Recursive:
    def __init__(self, graph, s):
        self.marked_array = [False]*graph.V()
        self.count_connected = 0
        
        self.dfs(graph, s)
    
    def dfs(self, graph, v):
        self.marked_array[v] = True
        self.count_connected += 1
        bag_ll = graph.adj[v]
        # I implemented the bag_linkedlist data structure to be iterable (each iteration returns the item instance variable which in this case corresponds to the vertex).
        for neighbor_vertex in bag_ll:
            if self.marked_array[neighbor_vertex]: 
                print(neighbor_vertex,'is already marked.')
            else:
                print("dfs(",neighbor_vertex,")")
                self.dfs(graph, neighbor_vertex)

    # Is v connected to s?
    def marked(self, v):
        return self.marked_array[v]

    # number of vertices connected to s (including s)     
    def count(self):
        return self.count_connected
    
    
    
def main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    graph = Graph_Array_AdjacencyLists(filename=filename, delimiter=delimiter)
    s = int(sys.argv[3])
    
    dfs_structure = DFS_Recursive(graph,s)
    
    for i in range(4,4+len(sys.argv[4:])):
        v = int(sys.argv[i])
        print(v,"connected to", s,": ", dfs_structure.marked(v))
    
    print("number of vertices connected to", s,": ", dfs_structure.count())
   


if __name__=="__main__": main()