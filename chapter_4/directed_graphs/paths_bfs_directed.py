# Title: paths_bfs_directed.py
# Author: Ryan Borchardt

# The implementation uses an iterative implementation of breadth first search.

# This class extends the functionality of directed graphs to be able to:
# 1. Determine if a directed path from a source vertex to a given target vertex exists (single-source reachability)
# 2. If a path exists, find the shortest path. 

# Example:
# python paths_bfs_directed.py tinyDG.txt ' '


import sys

from chapter_4.directed_graphs.digraph import Digraph
from chapter_1.stack.stack_resizingarray import Stack_ResizingArray
from chapter_1.queue.queue_linkedlist import Queue_LinkedList

class Paths_BFS_Directed:
    def __init__(self, digraph, s):
        self.marked_array = [False]*digraph.V()
        self.paths_array = [None]*digraph.V()
        self.s = s
        
        self.marked_array[self.s] = True
        self.bfs(self.s, digraph)
        
    def bfs(self,v, digraph): 
        queue = Queue_LinkedList()
        queue.enqueue(v)
        while queue:
            v = queue.dequeue()
            for points_towards in digraph.adjacent(v):
                if not self.marked_array[points_towards]:
                    self.marked_array[points_towards] = True
                    self.paths_array[points_towards] = v
                    queue.enqueue(points_towards)
        
    
    
    def hasPathTo(self, v):
        return self.marked_array[v]
        
    def pathTo(self,v):
        if not self.hasPathTo(v): return None
        stack = Stack_ResizingArray()
        
        while v is not None:
            stack.push(v)
            v = self.paths_array[v]
        return stack
        
        



def main():
    digraph = Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    
    paths_bfs = Paths_BFS_Directed(digraph, s=7)
    #print(paths_bfs.marked_array)
    #print(paths_bfs.paths_array)
    print("Path from 7 to 3?", paths_bfs.hasPathTo(3))
    print('\n\nPath from 7 to 3:')
    print(paths_bfs.pathTo(3))
    
if __name__=="__main__": main()