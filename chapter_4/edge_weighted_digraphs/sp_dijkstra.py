"""
Title: sp_dijkstra.py
Author: Ryan Borchardt

Implementation of API on page 645.

Assumptions: 
1. non-negative edges


Time complexity: Proportional to E*lg(V) + V*lg(V)
    V delMin() operations (each lg(V))
    V calls to relax: where each relax() call takes E/V*lg(V) time in the worst case
Space complexity: Proportional to V
    the _distTo and edgeTo arrays have length V
    the indexed priority queue has length V and is represented by three arrays of length V (the binary heap array, the key array and the inverted index array)

Example:
python sp_dijkstra.py tinyEWD.txt ' ' 0

"""

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray
from algorithms_python.chapter_4.edge_weighted_digraphs.directed_edge import Directed_Edge
from algorithms_python.chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph
from algorithms_python.chapter_2.priority_queue.indexed_priorityqueue_min_standard import Indexed_PriorityQueue_Min


class Shortest_Paths:
    def __init__(self, ewdg, s):
        self._distTo = [float('inf') for i in range(ewdg.V())]
        self._distTo[s] = 0
        
        self.edgeTo = [None]*ewdg.V()
              
        self.s = s
        # some way of determining the order methodology of choosing v:
        
        self.ipq = Indexed_PriorityQueue_Min(max_nodes=ewdg.V())
        self.ipq.insert(self.s,0)
        

        while self.ipq.isEmpty()==False:
            # self.ipq.delMin() returns the vertex with the smallest distance value.
            print('Indexed priority queue:')
            print(self.ipq)
            v = self.ipq.delMin()
            self.relax(ewdg,v)
    
    # vertex or edge relaxation
    def relax(self, ewdg, v):
        print('The shortest path to vertex ', v, 'has been permanently determined.')
        print("from vertex: ",v)
        for edge in ewdg.adjacent(v):
            print('Edge: ', edge)
            v = edge.from_vert()
            w = edge.towards_vert()
            
            if self._distTo[v] + edge.weight() < self._distTo[w]:
                print('This edge is eligible and will be relaxed')
                self.edgeTo[w] = edge
                
                self._distTo[w] = self._distTo[v] + edge.weight()
                print("towards vertex", w)
                if self.ipq.contains(w):
                    print('The vertex is already on the priority queue')
                    self.ipq.change(w,self._distTo[w])
                else:
                    print('The vertex was not on the priority queue')
                    self.ipq.insert(w,self._distTo[w])
            else:
                print('This edge is ineligible')
        print('\n')

            
        
    
    def distTo(self, v):
        return self._distTo[v]
        
    def hasPathTo(self,v):
        return self._distTo[v] != float('inf')
        
    # Returns stack of directed edges from the source vertex s to a given vertex v.    
    def pathTo(self,v):
        path_stack = Stack_ResizingArray()
        directed_edge = self.edgeTo[v]
        if v == self.s:
            return "No edges required to reach source vertex from source vertex"
        vert_from = directed_edge.from_vert()
        while vert_from != self.s:
            path_stack.push(directed_edge)
            directed_edge = self.edgeTo[vert_from]
            vert_from = directed_edge.from_vert()
        path_stack.push(directed_edge)
        return path_stack



def main():
    
    ewdg = Edge_Weighted_Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    source_vertex = int(sys.argv[3])
    sp = Shortest_Paths(ewdg, source_vertex)
    
    
    for i in range(ewdg.V()):
        print("Shortest path from ", source_vertex, " to ", i, ":")
        print(sp.pathTo(i))
        print("Total cost:", sp.distTo(i))
        print("\n\n")

        


if __name__== "__main__": main()