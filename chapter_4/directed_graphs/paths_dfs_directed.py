# Title: paths_dfs_directed.py
# Author: Ryan Borchardt

# This class extends the functionality of directed graphs to be able to:
# 1. Determine if a directed path from a source vertex to a given target vertex exists (single-source reachability)
# 2. If a path exists, find it. 

# Example:
# python paths_dfs_directed.py tinyDG.txt ' '


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.directed_graphs.digraph import Digraph
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray

class Paths_DFS_Directed:
    def __init__(self, digraph, s):
        self.digraph = digraph
        self.marked_array = [False]*self.digraph.num_V()
        self.paths_array = [None]*self.digraph.num_V()
        self.s = s
        self.marked_array[self.s] = True
        self.dfs(self.s)
        
    def dfs(self,v): 
        for points_towards in self.digraph.adjacent(v):
            if self.marked_array[points_towards] == False:
                self.marked_array[points_towards] = True
                self.paths_array[points_towards] = v
                self.dfs(points_towards)
        
    
    
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
    
    paths_dfs = Paths_DFS_Directed(digraph, s=7)
    #print(paths_dfs.marked_array)
    #print(paths_dfs.paths_array)
    print("Path from 7 to 3?", paths_dfs.hasPathTo(3))
    print('\n\nPath from 7 to 3:')
    print(paths_dfs.pathTo(3))
    
if __name__=="__main__": main()