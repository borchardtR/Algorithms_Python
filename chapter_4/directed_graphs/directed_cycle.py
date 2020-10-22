# Title: directed_cycle.py
# Author: Ryan Borchardt

# The implementation uses a recursive implementation of depth first search.

# This class extends the functionality of directed graphs to be able to:
# 1. Determine if a cycle exists in the digraph.
# 2. If a cycle exists, list a cycle (just one) in the digraph.

# Example:
# python directed_cycle.py tinyDG.txt ' '
# python directed_cycle.py tinyDAG.txt ' ' 


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.directed_graphs.digraph import Digraph
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray

class Directed_Cycle:
    def __init__(self, digraph):
        # This is used to keep track of whether a vertex has been encountered or not.
        # This way dfs() will only run at most once for each vertex
        self.marked_array = [False]*digraph.V()
        
        # This array is used to build the cycle_stack
        # For a given index
        self.paths_array = [None]*digraph.V()
        
        # This stack stays empty until a cycle is detected.
        # If a cycle is detected, all of the vertices along the cycle are added to the stack
        # This is done by utilizing the paths_array which stores the previous vertex along its path
        self.cycle_stack = Stack_ResizingArray()
        
        # This array keeps track of whether a vertex is still on the call stack.
        # If we encounter a vertex that is still on the call stack, then we know a cycle exists (similar to how if the end of the string re-encounters the string in the Tremaux maze)
        # The value at a given index is turned to True while it is on the call stack and turned to False when dfs finishes (and it is no longer on the call stack)
        self.onStack = [False]*digraph.V()
        
        for i in range(digraph.V()):
            # This way dfs goes through all vertices even if in different components.
            if self.marked_array[i] != True:
                self.dfs(i, digraph)
        
    def dfs(self,v, digraph):
        self.onStack[v] = True
        self.marked_array[v] = True
        for vertex in digraph.adjacent(v):
            # 1.
            # If a cycle has already been detected (and consequently cycle_stack has been built),
            # Then no more calls to dfs() will be added to the call stack and those remaining are quickly finished w/ this return statement.
            if self.hasCycle()==True: return
            
            # 2.
            # If a vertex has already been encountered, then we don't need to re-search through its neighbors.
            # We only search through the neighbors of a vertex once.
            elif self.marked_array[vertex] == False:
                self.paths_array[vertex] = v
                self.dfs(vertex, digraph)
            
            # 3.
            # If this is a true, a cycle has been detected and we can build the cycle stack to show the cycle.
            elif self.onStack[vertex] == True:
                self.cycle_stack.push(vertex)
                x = v
                while x != vertex:
                    self.cycle_stack.push(x)
                    x = self.paths_array[x]
                self.cycle_stack.push(vertex)
        
        self.onStack[v] = False
    
    
        
    
    
    def hasCycle(self):
        return not self.cycle_stack.isEmpty()
        
    def cycle(self):
        if self.hasCycle() == False: 
            return None
        else: 
            return self.cycle_stack
        
        



def main():
    digraph = Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    dc = Directed_Cycle(digraph)
    print('Does the digraph have a cycle?', dc.hasCycle())
    print('Cycle in digraph:')
    print(dc.cycle())

    
if __name__=="__main__": main()