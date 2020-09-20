# Title: mst_lazyprim.py
# Author: Ryan Borchardt


# Example:
# python mst_lazyprim.py tinyEWG.txt ' '


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.edge_weighted_graphs.edge import Edge
from algorithms_python.chapter_1.edge_weighted_graphs.edge_weighted_graph import Edge_Weighted_Graph
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList
# Created this class specifically for this module
from algorithms_python.chapter_2.priority_queue.priorityqueue_min_binaryheap import PriorityQueue_Min_BinaryHeap


class MST_LazyPrim:
    def __init__(self, ewg):
    
    # returns iterable of all edges in the MST 
    def edges(self):
        return 0
    
    def weight(self):
        return 0


def main():
    ewg = Edge_Weighted_Graph(filename=sys.argv[1], delimiter=sys.argv[2])
    mst = MST_LazyPrim(ewg)
        


if __name__=="__main__": main()