# Title: mst_eagerprim.py
# Author: Ryan Borchardt

# Determines the minimum spanning tree of an edge weighted graph using Prim's (eager) implementation.

"""
Time complexity: Proportional to V*lg(V) + E*lg(V)
    V time to build empty distTo and edgeTo (w/ V None placeholders)
    V*lg(V) time to build empty indexed priority queue (w/ V float('inf' placeholders)
    V*lg(V) for the V total delMin() operations 
    E*lg(V) for the V total visit() operations where each (on average) consists of average_degree change() operations
        # average degree for a graph = 2E/V, the change() operation takes lg(V) time for each
        # So V * 2E / V * lg(V) = E*lg(V)
    

Space complexity: Proportional to V.
    The arrays edgeTo and distTo have length V.
    The indexed priority queue consists of three arrays which each have length V in the worst case.

"""


# Example:
# python mst_eagerprim.py tinyEWG.txt ' '


import sys

from chapter_4.edge_weighted_graphs.edge import Edge
from chapter_4.edge_weighted_graphs.edge_weighted_graph import Edge_Weighted_Graph
#from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList
# Created this class specifically for MST
from chapter_2.priority_queue.indexed_priorityqueue_min_standard import Indexed_PriorityQueue_Min


class MST_EagerPrim:
    def __init__(self, ewg):
        
        self.edgeTo = [None]*ewg.V()
        self.distTo = [float('inf')]*ewg.V()
        
        self.priority_queue = Indexed_PriorityQueue_Min(max_nodes = ewg.V())
        for i in range(ewg.V()):
            self.priority_queue.insert(i, float('inf'))
        
        # 0 is the first vertex to the MST:
        self.distTo[0] = 0
        self.priority_queue.change(0,0)
        
        counter = 1
        while self.priority_queue.isEmpty() == False:
            print('\n\n\n','Iteration: ', counter)
            print('current indexed priority queue:')
            print(self.priority_queue)
            vertex = self.priority_queue.delMin()
            self.visit(ewg, vertex)
            counter+= 1
    
    def visit(self, ewg, vertex):
        print('Vertex ', vertex, ' has been added to the MST (and removed from the indexed priority queue).')
        # Remove this vertex (index) from the priority queue:
        
        
        for edge in ewg.adjacent(vertex):
            towards_vert = edge.other(vertex)
            
            
            if (edge.weight() < self.distTo[towards_vert]) and (self.priority_queue.contains(towards_vert)):
                print('Edge from ', vertex, ' to ', towards_vert, 'is eligible.')
                self.edgeTo[towards_vert] = edge
                self.distTo[towards_vert] = edge.weight()
                self.priority_queue.change(towards_vert, edge.weight())
            
            else:
                print('Edge from ', vertex, ' to ', towards_vert, 'is NOT eligible.') 
                
            
        
        
    # returns iterable of all edges in the MST 
    def edges(self):
        return self.edgeTo[1:]
    
    def weight(self):
        total_weight = 0
        for edge in self.edgeTo[1:]:
            total_weight += edge.weight()
            
        return total_weight


def main():
    ewg = Edge_Weighted_Graph(filename=sys.argv[1], delimiter=sys.argv[2])
    mst = MST_EagerPrim(ewg)
    
    print('Edges in MST:')
    for edge in mst.edges():
        print(edge)
    
    print('Weight of MST:')
    print(mst.weight()) 


if __name__=="__main__": main()