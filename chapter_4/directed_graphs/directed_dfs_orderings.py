# Title: directed_dfs_orderings.py
# Author: Ryan Borchardt

# sorts the vertices of the directed graph in the following orders:

# 1. Preorder: The order of the dfs() calls
# 2. Postorder: The order in which the dfs() calls finish.
# 3. Reverse postorder: This is the topological order of the digraph (order that allows for all directed edges to point from a vertex already earlier in the order).

# Time complexity: Proportional to V + E
# Space complexity: Proportional to V 


# Example:
# python directed_dfs_orderings.py tinyDG.txt ' '
# python directed_dfs_orderings.py tinyDAG.txt ' '

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.directed_graphs.digraph import Digraph
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList


class Directed_DFS_Orderings:
    def __init__(self, digraph):
        self.marked_array = [False]*digraph.V()
        
        self.pre_order = Queue_LinkedList()
        self.post_order = Queue_LinkedList()
        self.reverse_post_order = Stack_ResizingArray()
        
        for i in range(digraph.V()):
            if self.marked_array[i] != True:
                self.dfs(i, digraph)
        
        
    def dfs(self,v, digraph):
        self.pre_order.enqueue(v)
        self.marked_array[v] = True
        for j  in digraph.adjacent(v):
            if self.marked_array[j] != True:
                self.dfs(j, digraph)
        self.post_order.enqueue(v)
        self.reverse_post_order.push(v)
    
    def preorder(self):
        return self.pre_order
    
    def postorder(self):
        return self.post_order        
    
    def reversepostorder(self):
        return self.reverse_post_order 

        



def main():
    digraph = Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    
    dfs_orderings = Directed_DFS_Orderings(digraph)
    
    print("Preorder:")
    print(dfs_orderings.preorder())
    
    print("Postorder:")
    print(dfs_orderings.postorder())
    
    print("Reverse postorder:")
    print(dfs_orderings.reversepostorder())
    
if __name__=="__main__": main()