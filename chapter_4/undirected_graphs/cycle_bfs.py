# Title: cycle_bfs.py
# Author: Ryan Borchardt

# This implementation utilizes breadth first search.
# The breadth first search version of this program requires an extra array (of length V) of space in order to store the previous vertex.

# This class extends the functionality of undirected graphs to be able to:
# 1. Determine if a graph contains a cycle or if it is acyclic.


# Example:
# python cycle_bfs.py tinyG.txt ' '
#


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.undirected_graphs.graph_array_adjacencylists import Graph_Array_AdjacencyLists
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList

class Cycle:
    def __init__(self, graph):
        self._marked_array = [False]*graph.V()
        self.prev_vertex = [None]*graph.V()
        self.has_cycle = False
        for i in range(graph.V()):
            if self._marked_array[i] == False:
                self.bfs(graph, i)
    
    def bfs(self, graph, v):
        queue = Queue_LinkedList()
        queue.enqueue(v)
        
        while queue.isEmpty() == False:
            v = queue.dequeue()
            if self._marked_array[v] == True:
                continue 
            self._marked_array[v] = True
            neighbors = graph.adjacent(v)
            for neighbor in neighbors:
                if (self._marked_array[neighbor] == True) and (neighbor != self.prev_vertex[v]):
                    self.has_cycle = True
                if self._marked_array[neighbor] == False:
                    queue.enqueue(neighbor)
                    self.prev_vertex[neighbor] = v
    
    def hasCycle(self):
        return self.has_cycle
        
        
def main():
    graph = Graph_Array_AdjacencyLists(filename=sys.argv[1], delimiter=sys.argv[2])
    cycle = Cycle(graph)
    print('This graph contains a cycle?:', cycle.hasCycle())
    

if __name__=="__main__": main()