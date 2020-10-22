# Title: connected_components_bfs.py
# Author: Ryan Borchardt

# This implementation utilizes breadth first search.

# This class extends the functionality of undirected graphs to be able to:
# 1. Determine if a path exists from a vertex to another vertex.
# 2. Determine which component a vertex is part of.
# 3. Determine the number of components in the graph.

# Time complexity: Proportional to V + E 
# Space complexity: Proportional to V

# Example:
# python connected_components_bfs.py tinyG.txt ' '

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.undirected_graphs.graph_array_adjacencylists import Graph_Array_AdjacencyLists
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList

class CC:
    def __init__(self, graph):
        self._marked_array = [False for i in range(graph.V())]
        self._id = [None for i in range(graph.V())]
        self._count = -1
        
        for i in range(graph.V()):
            if self._marked_array[i] == False:
                self._count += 1
                self.bfs(graph, i)
            
    def bfs(self, graph, v):
        queue = Queue_LinkedList()
        queue.enqueue(v)
        
        while queue.isEmpty() == False:
            v = queue.dequeue()
            if self._marked_array[v] == True:
                continue
            self._marked_array[v] = True
            
            self._id[v] = self._count
            neighbors = graph.adjacent(v)
        
            for neighbor in neighbors:
                if self._marked_array[neighbor] == False:
                    queue.enqueue(neighbor)
                
        
        
    def connected(self, v, w):
        return self._id[v] == self._id[w] 
    
    def count(self):
        return self._count+1 
    
    def id(self, v):
        return self._id[v]
        

def main():
    graph = Graph_Array_AdjacencyLists(filename = sys.argv[1], delimiter = sys.argv[2])
    cc = CC(graph)
    
    print('component count:', cc.count())
    print('id of vertex 8:', cc.id(8))
    print('Vertex 0 connected to vertex 4?', cc.connected(0,4))
    print('Vertex 0 connected to vertex 8?', cc.connected(0,8))

if __name__ == "__main__": main() 