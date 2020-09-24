"""
Title: shortest_paths.py
Author: Ryan Borchardt

# Implementation of API on page 645.





    # Lets say we are dealing with an edge-weighted digraph and want a priority queue of vertices based on their current distance from s.
    # The priority level is determined by their current distance from s.
    
    # 1. But how do we efficiently determine which vertex is associated with a distance that gets removed from delMin?? How do we effeicently update the distance for a certain vertex?
        # A. Could use a symbol table where keys are priority levels which in this case is distances, and values are the vertices: 
                # No b/c there may be multiples of the same distance ie 'inf' and you can't have multiples of keys...
        # B. Could create a Vertex object where it has an instance variable for distance and is comparable based on that distance. Add vertices to a priority queue.
                # Requires going back and redefining the Directed_Edge and Edge_Weighted_Digraph and makes them more complicated.
        # C. Could go through the distTo() array and sequentially seach for the minimum distance (its index = the vertex it corresponds to) requires another array that marks if vertex has been visited. No priority queue is needed.
            # Sequential search takes linear (V) time. Could be faster (see below).
        # D. Could create an indexed priority queue where the priority queue is still ordered based on distance but each distance is associated with an integer (vertex).
            # Returning (and deleting) the min takes lg(V) time. (Inserting takes longer than method C but the overall time complexity for D is still lower




Example:
python shortest_paths.py tinyEWD.txt ' ' 0

"""

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_1.bag.bag_linkedlist import Bag_LinkedList
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray
from algorithms_python.chapter_4.edge_weighted_digraphs.directed_edge import Directed_Edge
from algorithms_python.chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph


class Shortest_Paths:
    def __init__(self, ewdg, s):
        self._distTo = [float('inf') for i in range(ewdg.V())
        self._distTo[s] = 0
        
        self.edgeTo = [None]*ewdg.V()
              
        # some way of determining the order methodology of choosing v:
        self.relax(ewdg,v)
    
    # vertex or edge relaxation
    def relax(self, ewdg, v):
        
    
    def distTo(self, v):
        return self._distTo[v]
        
    def hasPathTo(self,v):
        return self._distTo[v] != float('inf')
        
    # Returns stack of directed edges from the source vertex s to a given vertex v.    
    def pathTo(self,v):
        path_stack = Stack_ResizingArray()
        directed_edge = edgeTo[v]
        vert_from = directed_edge.from_vert()
        while vert_from != self.s:
            path_stack.push(directed_edge)
            directed_edge = edgeTo[vert_from]
            vert_from = directed_edge.from_vert()
        path_stack.push(directed_edge)
        return path_stack



def main():
    
    ewdg = Edge_Weighted_Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    
    sp = Shortest_Paths(ewdg, sys.argv[3])
    
    
    print(ewdg.V())
    print(ewdg.E())
    print(ewdg)
    
    for i in ewdg.edges():
        print(i)
        


if __name__=="__main__": main()