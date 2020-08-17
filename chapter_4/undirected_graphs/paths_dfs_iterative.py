# Title: paths_dfs_iterative.py
# Author: Ryan Borchardt

# This implementation builds off of the code in dfs_iterative.py

# This class extends the functionality of undirected graphs to be able to:
# 1. Determine if a path exists from a vertex to another vertex (using the same dfs algorithm as in dfs_recursive.py and dfs_iterative.py).
# 2. Determine a path between two connected vertices.  


# Example 2:
# python paths_dfs_iterative.py tinyCG.txt ' ' 0

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/Ryan/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.undirected_graphs.graph_arraylinkedlists import Graph_ArrayLinkedLists
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray

class Paths_dfs:
    def __init__(self, graph, s):
        self.path_array = [None]*graph.num_V()
        self.marked_array = [False]*graph.num_V()
        self.s = s
        
        self.dfs(graph, s)
    
    def dfs(self, graph, v):
        self.marked_array[v] = True
        stack = Stack_ResizingArray()
        stack.push(v)
        while stack.isEmpty() == False:
            vertex = stack.pop()
            self.marked_array[vertex] = True
            neighbors_list = graph.adj[vertex]
            for i in neighbors_list:
                if self.marked_array[i] != True:
                    stack.push(i)
                    self.path_array[i] = vertex
    
    def hasPathTo(self, v):
        return self.marked_array[v]
        
    def pathTo(self,v):
        if self.hasPathTo(v) == False: return None
        stack = Stack_ResizingArray()
        x = v
        while x != self.s:
            stack.push(x)
            x = self.path_array[x]
        stack.push(self.s)
        return stack
        
def main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    graph = Graph_ArrayLinkedLists(filename=filename, delimiter=delimiter)
    s = int(sys.argv[3])
    
    paths = Paths_dfs(graph,s)
    
    print(paths.marked_array)
    
    print(paths.path_array)
    
    print(paths.pathTo(0))
    
    # the pathTo() method returns a stack object (which I have designed to be iterable) so for i in stack_object iterates through the items in each node of the bag
    for i in range(graph.num_V()):
        string = "0 to " + str(i) +": "
        for j in paths.pathTo(i):
            if j != i:
                string = string + str(j) + "->"
            else:
               string = string + str(j)
        print(string)

if __name__=="__main__":
    main()