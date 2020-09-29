# Title: directed_weighted_cycle.py
# Author: Ryan Borchardt

# This implementation extends the cycle detection functionality from unweighted digraphs (see directed_cycle.py) to weighted digraphs

# This class extends the functionality of weighted digraphs to be able to:
# 1. Determine if a cycle exists in the weighted digraph.
# 2. If a cycle exists, list a cycle (just one) in the weighted digraph.

# Example:
# python directed_weighted_cycle.py tinyEWD.txt ' '
# python directed_weighted_cycle.py tinyEWDAG.txt ' ' 


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray

class Directed_Weighted_Cycle:
    def __init__(self, ew_digraph):
        self.ew_digraph = ew_digraph
        # This is used to keep track of whether a vertex has been encountered or not.
        # This way dfs() will only run at most once for each vertex
        self.marked_array = [False]*self.ew_digraph.V()
        
        # This array is used to build the cycle_stack
        # For a given index
        self.paths_array = [None]*self.ew_digraph.V()
        
        # This stack stays empty until a cycle is detected.
        # If a cycle is detected, all of the vertices along the cycle are added to the stack
        # This is done by utilizing the paths_array which stores the previous vertex along its path
        self.cycle_stack = Stack_ResizingArray()
        
        # This array keeps track of whether a vertex is still on the call stack.
        # If we encounter a vertex that is still on the call stack, then we know a cycle exists (similar to how if the end of the string re-encounters the string in the Tremaux maze)
        # The value at a given index is turned to True while it is on the call stack and turned to False when dfs finishes (and it is no longer on the call stack)
        self.onStack = [False]*self.ew_digraph.V()
        
        for i in range(self.ew_digraph.V()):
            # This way dfs goes through all vertices even if in different components.
            if self.marked_array[i] != True:
                self.dfs(i)
        
    def dfs(self,v):
        self.onStack[v] = True
        self.marked_array[v] = True
        
        # For Edge_Weighted_Digraph, self.ewdigraph.adjacent(v) returns the edges coming from vertex v (in Digraph, self.digraph.adjacent(v) returns the vertices v is pointing towards.
        for directed_edge in self.ew_digraph.adjacent(v):
            w = directed_edge.towards_vert()
            
            # 1.
            # If a cycle has already been detected (and consequently cycle_stack has been built),
            # Then no more calls to dfs() will be added to the call stack and those remaining are quickly finished w/ this return statement.
            if self.hasCycle()==True: return
            
            # 2.
            # If a vertex has already been encountered, then we don't need to re-search through its neighbors.
            # We only search through the neighbors of a vertex once.
            elif self.marked_array[w] == False:
                self.paths_array[w] = v
                self.dfs(w)
            
            # 3.
            # If this is a true, a cycle has been detected and we can build the cycle stack to show the cycle.
            elif self.onStack[w] == True:
                self.cycle_stack.push(w)
                x = v
                while x != w:
                    self.cycle_stack.push(x)
                    x = self.paths_array[x]
                self.cycle_stack.push(w)
        
        self.onStack[v] = False
    
    
        
    
    
    def hasCycle(self):
        return not self.cycle_stack.isEmpty()
        
    def cycle(self):
        if self.hasCycle() == False: 
            return None
        else: 
            return self.cycle_stack
        
        



def main():
    ew_digraph = Edge_Weighted_Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    dc = Directed_Weighted_Cycle(ew_digraph)
    print('Does the digraph have a cycle?', dc.hasCycle())
    print('Cycle in digraph:')
    print(dc.cycle())

    
if __name__=="__main__": main()