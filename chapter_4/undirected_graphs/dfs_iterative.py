# Title: depthfirstsearch_undirected.py
# Author: Ryan Borchardt

# This is the iterative version of dfs.py
# I did this to explicitly show the usage of a stack to implement dfs (the recursive version uses the call stack).

# Example 1:
# python dfs_iterative.py tinyCG.txt ' ' 0 2 5

import sys
sys.path.append('C:/Users/Ryan/Desktop/Work/')
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray
from algorithms_python.chapter_4.undirected_graphs.graph_arraylinkedlists import Graph_ArrayLinkedLists

class Depth_First_Search:
    def __init__(self, graph, s):
        self.marked_array = [False]*graph.num_V()
        self.count_connected = 0
        
        self.dfs(graph,s)
    
    def dfs(self,graph,s):
        stack = Stack_ResizingArray()
        stack.push(s)
        while stack.isEmpty() != True:
            v = stack.pop()
            # Need to check to see if this vertex has already been marked (this would occur if the vertex was already popped from the stack):
            if self.marked_array[v] == True:
                continue
            self.marked_array[v] = True
            self.count_connected += 1
            print(v, self.count_connected)
            for neighbor in graph.adj[v]:
                if self.marked_array[neighbor] != True:
                    stack.push(neighbor)
    
    def marked(self,v):
        return self.marked_array[v]
    
    def count(self):
        return self.count_connected
        
def main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    graph = Graph_ArrayLinkedLists(filename=filename, delimiter=delimiter)
    s = int(sys.argv[3])
    
    dfs_structure = Depth_First_Search(graph,s)
    
    for i in range(4,4+len(sys.argv[4:])):
        v = int(sys.argv[i])
        print(v,"connected to", s,": ", dfs_structure.marked(v))
    
    print("number of vertices connected to", s,": ", dfs_structure.count())
    print(dfs_structure.marked_array)
   


if __name__=="__main__": main()