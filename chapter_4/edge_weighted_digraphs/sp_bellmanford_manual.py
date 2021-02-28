"""
Title: sp_bellmanford_manual.py
Author: Ryan Borchardt

Implementation of API on page 645.

Assumes no negative cycles reachable from s.

Takes space proportional to V.

Takes time proportional to E*V (all cases).
    Does V passes where all E edges are examined to see if they are eligible to relaxed (and subsequently relaxed if they are eligible).



Example:
python sp_bellmanford_manual.py tinyEWDn.txt ' ' 0
python sp_bellmanford_manual.py tinyEWDn.txt ' ' 5

"""

import sys
from chapter_1.stack.stack_resizingarray import Stack_ResizingArray
from chapter_4.edge_weighted_digraphs.directed_edge import Directed_Edge
from chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph



class Shortest_Paths:
    def __init__(self, ewdg, s):
        self._distTo = [float('inf') for i in range(ewdg.V())]
        self._distTo[s] = 0
        
        self.edgeTo = [None]*ewdg.V()
              
        self.s = s
        
        # some way of determining the order methodology of choosing v
            # in this case, we choose V arbitrarily and make up for it by doing EV passes.
        for i in range(ewdg.V()):
            print('\n')
            print('Pass: ', i+1)
            for j in range(ewdg.V()):
                for directed_edge in ewdg.adjacent(j):
                    self.relax(directed_edge)
        
    
    # takes in an edge
    def relax(self, edge):
        v = edge.from_vert()
        w= edge.towards_vert()
        
        print('Edge from ', v, ' to ', w, ' with weight ', edge.weight())
        print('Current distance to ', w, ' : ', self._distTo[w])
        print('Proposed new distance: ', self._distTo[v] + edge.weight())
        # If this is true, the edge is eligible to be relaxed
        if self._distTo[v] + edge.weight()  < self._distTo[w]:
            print('This edge is eligible to relaxed')
            print('\n')
            self._distTo[w] = self._distTo[v] + edge.weight()
            self.edgeTo[w] = edge
            
        else:
            print('This edge is NOT eligible to be relaxed.')
            print('\n')

            
        
    
    def distTo(self, v):
        return self._distTo[v]
        
    def hasPathTo(self,v):
        return self._distTo[v] != float('inf')
        
    # Returns stack of directed edges from the source vertex s to a given vertex v.    
    def pathTo(self,v):
        path_stack = Stack_ResizingArray()
        directed_edge = self.edgeTo[v]
        if v == self.s:
            return "No edges required to reach source vertex from source vertex"
        vert_from = directed_edge.from_vert()
        while vert_from != self.s:
            path_stack.push(directed_edge)
            directed_edge = self.edgeTo[vert_from]
            vert_from = directed_edge.from_vert()
        path_stack.push(directed_edge)
        return path_stack



def main():
    
    ewdg = Edge_Weighted_Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    source_vertex = int(sys.argv[3])
    sp = Shortest_Paths(ewdg, source_vertex)
    
    for i in range(ewdg.V()):
        print("Shortest path from ", source_vertex, " to ", i, ":")
        print(sp.pathTo(i))
        print("Total cost:", sp.distTo(i))
        print("\n\n")

        


if __name__== "__main__": main()