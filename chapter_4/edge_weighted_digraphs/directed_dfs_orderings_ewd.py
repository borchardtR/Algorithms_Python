# Title: directed_dfs_orderings_ewd.py
# Author: Ryan Borchardt

# directed_dfs_orderings_ewd.py is adapted from directed_dfs_orderings.py to allow for determining the dfs orderings of an edge weighted digraph 

# sorts the vertices of an edge-weighted directed graph in the following orders:

# 1. Preorder: The order of the dfs() calls
# 2. Postorder: The order in which the vertices are done.
# 3. Reverse postorder: This is the topological order of the digraph (order that allows for all directed edges to point from a vertex already earlier in the order).

# Example:
# python directed_dfs_orderings_ewd.py tinyEWD.txt ' '
# python directed_dfs_orderings_ewd.py tinyEWDAG.txt ' '

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList


class Directed_DFS_Orderings_EWD:
    def __init__(self, ew_digraph):
        self.ew_digraph = ew_digraph
        self.marked_array = [False]*self.ew_digraph.V()
        
        self.pre_order = Queue_LinkedList()
        self.post_order = Queue_LinkedList()
        self.reverse_post_order = Stack_ResizingArray()
        
        for i in range(self.ew_digraph.V()):
            if self.marked_array[i] != True:
                self.dfs(i)
        
        
    def dfs(self,v):
        self.pre_order.enqueue(v)
        self.marked_array[v] = True
        
        # For Edge_Weighted_Digraph, self.ew_digraph.adjacent(v) returns the edges coming from vertex v (in Digraph, self.digraph.adjacent(v) returns the vertices v is pointing towards).    
        for directed_edge  in self.ew_digraph.adjacent(v):
            w = directed_edge.towards_vert()
            if self.marked_array[w] != True:
                self.dfs(w)
        self.post_order.enqueue(v)
        self.reverse_post_order.push(v)
    
    def preorder(self):
        return self.pre_order
    
    def postorder(self):
        return self.post_order        
    
    def reversepostorder(self):
        return self.reverse_post_order 

        



def main():
    ew_digraph = Edge_Weighted_Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    
    dfs_orderings = Directed_DFS_Orderings_EWD(ew_digraph)
    
    print("Preorder:")
    print(dfs_orderings.preorder())
    
    print("Postorder:")
    print(dfs_orderings.postorder())
    
    print("Reverse postorder:")
    print(dfs_orderings.reversepostorder())
    
if __name__=="__main__": main()