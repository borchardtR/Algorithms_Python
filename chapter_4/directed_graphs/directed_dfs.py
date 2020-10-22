# Title: directed_dfs.py
# Author: Ryan Borchardt

# The implementation uses a recursive implementation of depth first search.

# This class extends the functionality of directed graphs to be able to:
# 1. Determine if a directed path from a source vertex to a given target vertex exists (single-source reachability)
# 2. Determine if a directed path from any vertex in the source set to a given target vertex exists (multiple-source reachability)

# Example:
# python directed_dfs.py tinyDG.txt ' '


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.directed_graphs.digraph import Digraph

class Directed_DFS:
    def __init__(self, digraph, *args):
        self.marked_array = [False]*digraph.V()
        
        for s in args:
            self.marked_array[s] = True
            self.dfs(s,digraph)
        
    def dfs(self,v,digraph):
    
        for points_towards in digraph.adjacent(v):
            if self.marked_array[points_towards] == False:
                self.marked_array[points_towards] = True
                self.dfs(points_towards,digraph)
        
    
    
    def marked(self, v):
        return self.marked_array[v]
        
        



def main():
    digraph = Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    
    d_dfs_1 = Directed_DFS(digraph, 5)
    print(d_dfs_1.marked(0))
    print(d_dfs_1.marked(8))
    
    d_dfs_2 = Directed_DFS(digraph, 5,0,8,9)
    print(d_dfs_2.marked(4))
    print(d_dfs_2.marked(7))    
    
if __name__=="__main__": main()