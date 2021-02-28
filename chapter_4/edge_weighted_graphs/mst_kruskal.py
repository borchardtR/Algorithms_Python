# Title: mst_kruskal.py
# Author: Ryan Borchardt

# Determines the minimum spanning tree of an edge weighted graph using Kruskal's implementation.

"""
Building the MST using Kruskal's algorithm has time complexity:

= E*(lg(E) + lg(V)) + V*lg(V)
= E*lg(E) + E*lg(V) + V*lg(V)

E is at most = V^2, which means lg(E) is at most 2*lg(V)

So you can say: E <= V^2 and lg(E) <= 2*lg(V)

In other words, in the worst-case (when E is the greatest it can possibly be):

E = V^2 so lg(E) = 2*lg(V) 

Which is equivalent to saying :  V = E^(1/2) and lg(V) = 1/2*lg(E) 

Kruskal takes:
= E*lg(E) + E*lg(V) + V*lg(V)

Inserting for V and lg(V):

= E*lg(E) + E*1/2*lg(E)+ 1/2* (E^1/2) * lg(E) 

Which simplifies to:

O(E*lg(E)

The MST using Kruskal's algorithm has space complexity:

= V + E + V

Where in the worst case, E= V^2

= V^2 + V 

So the space complexity is V^2 in the worst case which is E.

O(E)
"""


# Example:
# python mst_kruskal.py tinyEWG.txt ' '


import sys

from chapter_4.edge_weighted_graphs.edge import Edge
from chapter_4.edge_weighted_graphs.edge_weighted_graph import Edge_Weighted_Graph
from chapter_1.queue.queue_linkedlist import Queue_LinkedList
from chapter_2.priority_queue.priorityqueue_min_binaryheap import PriorityQueue_Min_BinaryHeap
from chapter_1.union_find.uf_weightedquickunion import UF_WeightedQuickUnion

class MST_Kruskal:
    def __init__(self, ewg):
        self.mst_edges = Queue_LinkedList()
        self.edges_pq = PriorityQueue_Min_BinaryHeap()
        
        # Takes E*lg(E) time
        for edge in ewg.edges():
            self.edges_pq.insert(edge)
        # Note that we can construct a heap of size E in E time w/ heapq.heapify() (see algorithm for heap construction in heapsort)
        
        self.union_find = UF_WeightedQuickUnion(num_sites=ewg.V())    
        
        # Takes E*(lg(E) + lg(V)) + (V-1)*lg(V) time which simplies to ~ E*lg(E) time
        while self.edges_pq and len(self.mst_edges)<(ewg.V()-1):
            min_edge = self.edges_pq.delMin()
            # Before adding min_edge to self.mst_edges queue, need to confirm that adding this edge won't create a cycle:
            # Can do this by using Union Find data structure
            # If the two vertices are already connected in the union_find data structure, we know that adding an edge would create a cycle 
            vertex_1 = min_edge.either()
            vertex_2 = min_edge.other(vertex_1)
            if not self.union_find.connected(vertex_1,vertex_2):
                self.mst_edges.enqueue(min_edge)
                self.union_find.union(vertex_1, vertex_2)

        
    # returns iterable of all edges in the MST b/c self.mst_edges is a queue (which is an iterable object)
    # Takes V-1 time
    def edges(self):
        return self.mst_edges
    
    # Takes V-1 time
    def weight(self):
        total_weight = 0
        for edge in self.mst_edges:
            total_weight += edge.weight()
        return total_weight


def main():
    ewg = Edge_Weighted_Graph(filename=sys.argv[1], delimiter=sys.argv[2])
    mst = MST_Kruskal(ewg)
    
    print('Edges in MST:')
    print(mst.edges())
    
    print('Weight of MST:')
    print(mst.weight()) 


if __name__=="__main__": main()