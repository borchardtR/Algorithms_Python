# Title: symbol_graph.py
# Author: Ryan Borchardt

# I am implementing the graph data structure using an array of linked lists.
# This is an implementation of the graph API listed on page 522 of Sedgewick and Wayne's Algorithms. 
# This implementation is for: unweighted, undirected graphs that allows for self-loops and parallel edges.
# The names of the vertices are restricted to being integers from 0 to V-1 where V is the number of vertices in the graph.
    # See my alternate implementation (graph_alt.py) that allows for the names of the verticies to be any object. This implementation has additional functionality such as being able to...
# Note that Sedgewick and Wayne implement their graph data strucuture using the Bag data structure that was implemented with linked lists. 

# Note that Sedgewick and Wayne somtimes use the same name for both instance variables and instance methods (for example instance variable self.adj and instance method adj) in their Java code
    # In Python, the instance variable is called self.adj within the class definition and graph.adj in the test client (if the variable graph is a reference to a Graph_Array_AdjacencyLists object)
    # The instance method is called self.adj() within the class definition and graph.adj() in the test client
    # This can be problematic in Python b/c: The instance variable will ALWAYS be called when you intend to call the instance method if they share the same name
    # For example, graph.adj(0) in the test client is actually interpreted as applying (0) to the graph.adj instance variable rather than calling the graph.adj() instance method with 0 as an input
    # For clarity, I always make sure that instance variables and instance methods do not share the same name

# Space required: E + V
# Time to add edge v-w: 1
# Time to check whether w is adjacent to v: degree(v)
# Time to iterate through verticies adjacent to v: degree(v)

# Example:
# python symbol_graph.py tinyG.txt ' '

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/')
from algorithms_python.chapter_4.undirected_graphs.graph_array_adjacencylists import Graph_Array_AdjacencyLists
from algorithms_python.chapter_3.

class Symbol_Graph:
    def __init__(self, filename, delimiter):
        # Need to re-review chapter 3...
        self.st = ____
        self.inverted_index = [None]
        self.graph = Graph_Array_AdjacencyLists()
    
    def contains(self, key):
        return True
    
    def index(self, key):
        return 0
    
    def name(self, int):
        return 'key name'
        
    def G(self):
        return self.graph

def main():
    sg = Symbol_Graph(filename=sys.argv[1], delimiter=sys.argv[2])
        


if __name__=="__main__": main()





