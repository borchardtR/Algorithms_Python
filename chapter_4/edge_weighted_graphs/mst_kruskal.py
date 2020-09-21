# Title: mst_kruskal.py
# Author: Ryan Borchardt

# Determines the minimum spanning tree of an edge weighted graph using Kruskal's implementation.



# Example:
# python mst_kruskal.py tinyEWG.txt ' '


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.edge_weighted_graphs.edge import Edge
from algorithms_python.chapter_4.edge_weighted_graphs.edge_weighted_graph import Edge_Weighted_Graph
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList
# Created this class specifically for MST
from algorithms_python.chapter_2.priority_queue.priorityqueue_min_binaryheap import PriorityQueue_Min_BinaryHeap


class MST_Kruskal:
    def __init__(self, ewg):
        self.mst = Queue_LinkedList()
        
        self.edges_pq = PriorityQueue_Min_BinaryHeap()
        for edge in ewg.edges():
            self.edges_pq.insert(edge)
            
        # Instead of Union Find object, I used an undirected, unweighted graph along with 
        


        
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
    mst = MST_Kruskal(ewg)
    
    print('Edges in MST:')
    print(mst.edges())
    
    print('Weight of MST:')
    print(mst.weight()) 


if __name__=="__main__": main()