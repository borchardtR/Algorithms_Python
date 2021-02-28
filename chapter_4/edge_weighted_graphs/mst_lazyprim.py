# Title: mst_lazyprim.py
# Author: Ryan Borchardt

# Determines the minimum spanning tree of an edge weighted graph using Prim's (lazy) implementation.

# Takes E*lg(E) time (worst-case is E inserts() to minPQ of length E and E deletes of minPQ of length E ) and E space (worst-case is minPQ contains E edges)

"""
Time complexity: Proportional to E*lg(E)
    In the worst case there are: E delMin() operations and E insert operations (V*2E/V*lg(E) which is E*lg(E)
Space complexity: Proportional to E + V
    The mst_vertices array has length V, the mst_edges queue has length V-1 and the crossing_edges priority queue has length E in the worst case
"""


# Example:
# python mst_lazyprim.py tinyEWG.txt ' '


import sys

from chapter_4.edge_weighted_graphs.edge import Edge
from chapter_4.edge_weighted_graphs.edge_weighted_graph import Edge_Weighted_Graph
from chapter_1.queue.queue_linkedlist import Queue_LinkedList
# Created this class specifically for MST
from chapter_2.priority_queue.priorityqueue_min_binaryheap import PriorityQueue_Min_BinaryHeap


class MST_LazyPrim:
    def __init__(self, ewg):
        self.mst_vertices = [False]*ewg.V()
        self.mst_edges = Queue_LinkedList()
        self.crossing_edges = PriorityQueue_Min_BinaryHeap()
        
        self.visit(ewg, 0)
        while self.crossing_edges:
            min_weight_crossing_edge = self.crossing_edges.delMin()
            # Need to check for ineligible edges:
            vert_1 = min_weight_crossing_edge.either()
            vert_2 = min_weight_crossing_edge.other(vert_1)
            if self.mst_vertices[vert_1] and self.mst_vertices[vert_2]:
                continue
            else:
                self.mst_edges.enqueue(min_weight_crossing_edge)
                # Need to determine which vertex in min_weight_crossing_edge is not already in mst:
                if self.mst_vertices[vert_1]:
                    self.visit(ewg,vert_2)
                if self.mst_vertices[vert_2]:
                    self.visit(ewg,vert_1)

                
    def visit(self, ewg, vertex):
        # Add vertex to MST
        self.mst_vertices[vertex] = True
        
        # Add edges to verticies not currently in the MST
        # Note that some of the edges in the minPQ will become ineligible as more vertices are added to MST 
        # These ineligible edges are non-mst edges connecting vertices already in MST
        for edge in ewg.adjacent(vertex):
            if not self.mst_vertices[edge.other(vertex)]:
                self.crossing_edges.insert(edge)
        
    # returns iterable of all edges in the MST 
    def edges(self):
        return self.mst_edges
    
    def weight(self):
        total_weight = 0
        for edge in self.mst_edges:
            total_weight += edge.weight()
        return total_weight


def main():
    ewg = Edge_Weighted_Graph(filename=sys.argv[1], delimiter=sys.argv[2])
    mst = MST_LazyPrim(ewg)
    
    print('Edges in MST:')
    print(mst.edges())
    
    print('Weight of MST:')
    print(mst.weight()) 


if __name__=="__main__": main()