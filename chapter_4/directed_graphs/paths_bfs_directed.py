# Title: paths_bfs_directed.py
# Author: Ryan Borchardt

# The implementation uses an iterative implementation of breadth first search.

# This class extends the functionality of directed graphs to be able to:
# 1. Determine if a directed path from a source vertex to a given target vertex exists (single-source reachability)
# 2. If a path exists, find the shortest path. 

# Example:
# python paths_bfs_directed.py tinyDG.txt ' '


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.directed_graphs.digraph import Digraph
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList

class Paths_BFS_Directed:
    def __init__(self, digraph, s):
        self.digraph = digraph
        self.marked_array = [False]*self.digraph.num_V()
        self.paths_array = [None]*self.digraph.num_V()
        self.s = s
        
        self.marked_array[self.s] = True
        self.bfs(self.s)
        
    def bfs(self,v): 
        queue = Queue_LinkedList()
        queue.enqueue(v)
        while queue.isEmpty()==False:
            v = queue.dequeue()
            for points_towards in self.digraph.adjacent(v):
                if self.marked_array[points_towards] == False:
                    self.marked_array[points_towards] = True
                    self.paths_array[points_towards] = v
                    queue.enqueue(points_towards)
        
    
    
    def hasPathTo(self, v):
        return self.marked_array[v]
        
    def pathTo(self,v):
        if self.hasPathTo(v) == False: return None
        stack = Stack_ResizingArray()
        x = v
        while x != self.s:
            stack.push(x)
            x = self.paths_array[x]
        stack.push(self.s)
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