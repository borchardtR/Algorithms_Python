# Title: paths_bfs.py
# Author: Ryan Borchardt

# This implementation utilizes breadth first search.

# This class extends the functionality of undirected graphs to be able to:
# 1. Determine if a path exists from a vertex to another vertex.
# 2. Determine the shortest path between two connected vertices.  


# Example:
# python paths_bfs.py tinyCG.txt ' ' 0

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.undirected_graphs.graph_array_adjacencylists import Graph_Array_AdjacencyLists
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray

class Paths_bfs:
    def __init__(self, graph, s):
        self.path_array = [None]*graph.num_V()
        self.marked_array = [False]*graph.num_V()
        self.s = s
        
        self.bfs(graph, s)
    
    def bfs(self, graph, v):
        queue = Queue_LinkedList()
        self.marked_array[v] = True
        queue.enqueue(v)
        while queue.isEmpty() == False:
            vertex = queue.dequeue()
            print(vertex)
            neighbors_list = graph.adj[vertex]
            for i in neighbors_list:
                if self.marked_array[i] != True:
                    queue.enqueue(i)
                    self.marked_array[i] = True
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
    graph = Graph_Array_AdjacencyLists(filename=filename, delimiter=delimiter)
    s = int(sys.argv[3])
    
    paths = Paths_bfs(graph,s)
    
    print(paths.path_array)
    
    print(paths.pathTo(1))
    
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