# Title: biparite_bfs.py
# Author: Ryan Borchardt

# This implementation utilizes breadth first search.

# This class extends the functionality of undirected graphs to be able to:
# 1. Determine if a graph is biparite.


# Example:
# python biparite_bfs.py tinyG.txt ' '
#


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.undirected_graphs.graph_array_adjacencylists import Graph_Array_AdjacencyLists
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList

class Biparite:
    def __init__(self, graph):
        self.marked_array = [False]*graph.V()
        self.biparite_array = [False]*graph.V()
        self._isBiparite = True
        
        for i in range(graph.V()):
            if self.marked_array[i] == False:
                self.bfs(graph,i)
        
    
    def bfs(self, graph, v):
        queue = Queue_LinkedList()
        queue.enqueue(v)
        
        while queue.isEmpty() == False:
            v = queue.dequeue()
            if self.marked_array[v] == True:
                continue
            
            self.marked_array[v] = True
            
            neighbors = graph.adjacent(v)
            for neighbor in neighbors:
                if (self.marked_array[neighbor]==True) and (self.biparite_array[neighbor] == self.biparite_array[v]):
                    self._isBiparite = False
                
                if self.marked_array[neighbor]==False:
                    queue.enqueue(neighbor)
                    #self.previous_vertex_array[neighbor] = v
                    self.biparite_array[neighbor] = not self.biparite_array[v]
                
            
            
            
    
    def isBiparite(self):
        return self._isBiparite
	


def main():
    graph = Graph_Array_AdjacencyLists(filename=sys.argv[1], delimiter=sys.argv[2])
    
    bp = Biparite(graph)
    
    print(bp.isBiparite())

if __name__=="__main__":
    main()