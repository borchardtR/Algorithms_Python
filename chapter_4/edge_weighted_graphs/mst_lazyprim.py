# Title: mst_lazyprim.py
# Author: Ryan Borchardt

# Determines the minimum spanning tree of an edge weighted graph using Prim's (lazy) implementation.

# Takes E*lg(E) time (worst-case is E inserts() to minPQ of length E and E deletes of minPQ of length E ) and E space (worst-case is minPQ contains E edges)

"""
Building the MST using Prim's (lazy) algorithm has time complexity:

= E*lg(E) + E*lg(E)

b/c there E delMin() operations: E*lg(E) 
and E insert() operations in visit(): E*lg(E)

O(E*lg(E))


The MST using Prim's (lazy) algorithm has space complexity:

= V + V-1 + E

Where in the worst case, E= V^2

= V + V -1 + V^2

So the space complexity is V^2 in the worst case which is E.

O(E)
"""


# Example:
# python mst_lazyprim.py tinyEWG.txt ' '


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.edge_weighted_graphs.edge import Edge
from algorithms_python.chapter_4.edge_weighted_graphs.edge_weighted_graph import Edge_Weighted_Graph
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList
# Created this class specifically for MST
from algorithms_python.chapter_2.priority_queue.priorityqueue_min_binaryheap import PriorityQueue_Min_BinaryHeap


class MST_LazyPrim:
    def __init__(self, ewg):
        self.mst_vertices = [False]*ewg.V()
        self.mst_edges = Queue_LinkedList()
        self.crossing_edges = PriorityQueue_Min_BinaryHeap()
        
        self.visit(ewg, 0)
        while self.crossing_edges.isEmpty() != True:
            min_weight_crossing_edge = self.crossing_edges.delMin()
            # Need to check for ineligible edges:
            vert_1 = min_weight_crossing_edge.either()
            vert_2 = min_weight_crossing_edge.other(vert_1)
            if (self.mst_vertices[vert_1]==True) and (self.mst_vertices[vert_2]==True):
                continue
            
            self.mst_edges.enqueue(min_weight_crossing_edge)
            
            # Need to determine which vertex in min_weight_crossing_edge is not already in mst:
            if self.mst_vertices[vert_1]==True:
                self.visit(ewg,vert_2)
            if self.mst_vertices[vert_2]==True:
                self.visit(ewg,vert_1)

                
    def visit(self, ewg, vertex):
        # Add vertex to MST
        self.mst_vertices[vertex] = True
        
        # Add edges to verticies not currently in the MST
        # Note that some of the edges in the minPQ will become ineligible as more vertices are added to MST 
        # These ineligible edges are non-mst edges connecting vertices already in MST
        for edge in ewg.adjacent(vertex):
            if self.mst_vertices[edge.other(vertex)] == False:
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