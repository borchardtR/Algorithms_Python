"""
Title: sp_bellmanford.py
Author: Ryan Borchardt

Implementation of API on page 645 as well as the API listed on page 677.


All of the shortest-path algorithms utilize vertex/edge relaxation. 
The differences between the shortest-path algorithms are:
    1. the methodology that is used to determine the order/frequency of the vertices/edges to be (potentially) relaxed. 
    2. the assumptions / limitations of when the shortest-path algorithm will work.
    3. The time complexity
    4. The space complexity 

Dijkstra's algorithm:
    1. The order of the vertices to be (potentially) relaxed is determined by the vertex with the lowest distTo value on the indexed priority queue
        Once a vertex is pulled from the indexed priority queue, we know that we have found the shortest path for it 
            b/c every other possible path goes through a vertex that is currently on the indexed priority queue and all of those vertices already have a higher distTo value
        Each vertex only needs to be relaxed once (ie there is only one pass of edge relaxation before all of the edges are ineligible). 
    2. Edges must have non-negative weights.
    3. Time complexity: Proportional to E*lg(V) + V*lg(V) (linearithmic)
    4. Space complexity: Proportional to V (linear)
    
Acyclic algorithm:
    1. The order of the vertices to be relaxed is determined by the topological order.
        Once a vertex is pulled from the topological order, all of its possible paths have been examined and the shortest path has been selected
        Each vertex only needs to be relaxed once (ie there is only one pass of edge relaxation before all of the edges are ineligible). 
    2. The graph must be acyclic.
    3. Time complexity: Proportional to E + V (linear)
    4. Space complexity: Proportional to V (linear)
    
    
Bellman-Ford algorithm:
    1. The order of the vertices to be (potentially) relaxed is determined by the edges that were relaxed in the previous pass:
        (with first pass being the source vertex), for edges that were relaxed in the previous pass, the towards_vert will be (potentially) relaxed in the next pass
        There is a max of V passes (of edge relaxation) until no edge is eligible.
    2. The graph must not have negative cycle(s).
    3. Time complexity: Proportional to E*V (worst-case), proportional to E (best-case)
    4. Space complexity: Proportional to V (linear) 


Assumes there are no negative cycles reachable from s.
    If there are, the program will still run -> it will return the negative cycle instead of the shortest paths from s.


Takes space proportional to V.

Takes time proportional to E*V (worst-case).
    Does  a max of V passes (worst-case) where a max of E edges are examined in each pass (worst-case) to see if they are eligible to relaxed (and subsequently relaxed if they are eligible).

Note that I implemented this algorithm differently than Sedgewick and Wayne (in a way that is much more intuitive to me).
    I explicitly kept track of the number of "passes" in the algorithm (this is determined by the number of times self.num_rcip reaches 0.
    If the number of "passes" reaches a number greater than V, we know a negative cycle exisits.

    


Example:
python sp_bellmanford_2.py tinyEWDn.txt ' ' 0
python sp_bellmanford_2.py tinyEWDnc.txt ' ' 0
python sp_bellmanford_2.py mediumEWD.txt ' ' 0
python sp_bellmanford_2.py tinyEWDn.txt ' ' 5

"""

import sys

from chapter_1.stack.stack_resizingarray import Stack_ResizingArray
from chapter_4.edge_weighted_digraphs.directed_edge import Directed_Edge
from chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph
from chapter_1.queue.queue_linkedlist import Queue_LinkedList
from chapter_4.edge_weighted_digraphs.directed_weighted_cycle import Directed_Weighted_Cycle



class Shortest_Paths:
    def __init__(self, ewdg, s):
        self.dist = [float('inf') for i in range(ewdg.V())]
        self.dist[s] = 0
        
        self.edgeTo = [None]*ewdg.V()
        
        self.queue = Queue_LinkedList()
        self.queue.enqueue(s) 
        
        self.on_queue = [False]*ewdg.V()
        self.on_queue[s] = True
        
        # keeps track of the # of edges from source to vertex in shortest path (should be a max of V-1, otherwise we have a negative cycle)
        self.len_path=[float('inf')]*ewdg.V()
        self.len_path[s]=0
        
        self.cycle = False
        self.s=s
        while self.queue:
            
            u = self.queue.dequeue()
            self.on_queue[u]=False
            
            for edge in ewdg.adjacent(u):
                v=edge.towards_vert()
                weight=edge.weight()
                if self.dist[u]+weight < self.dist[v]:
                    self.dist[v] = self.dist[u]+weight
                    self.len_path[v] = self.len_path[u]+1
                    if self.len_path[v] >= ewdg.V():
                        self.cycle=True
                        print('Negative cycle detected')
                        return
                    self.queue.enqueue(v)
                    self.on_queue[v]=True
                    self.edgeTo[v]=edge
            
            
        
    
    def distTo(self, v):
        return self.dist[v]
        
    def hasPathTo(self,v):
        return self.dist[v] != float('inf')
        
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
    

    def hasNegativeCycle(self):
        return self.cycle
    
        
    def negativeCycle(self):
        return self.cycle
    
    



def main():
    
    ewdg = Edge_Weighted_Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    source_vertex = int(sys.argv[3])
    sp = Shortest_Paths(ewdg, source_vertex)
    
    if not sp.hasNegativeCycle():
        for i in range(ewdg.V()):
            print("Shortest path from ", source_vertex, " to ", i, ":")
            print(sp.pathTo(i))
            print("Total cost:", sp.distTo(i))
            print("\n\n")
        
    else:
        print("A negative cycle is reachable from the source vertex.")
        print("Shortest paths could not be found.")
        print("Negative cycle: ")
        print(sp.negativeCycle())

        


if __name__== "__main__": main()