"""
Title: sp_bellmanford.py
Author: Ryan Borchardt

Implementation of API on page 645 as well as the API listed on page 677.

Tests for negative cycles reachable from s.

Takes space proportional to V.

Takes time proportional to E*V (worst-case).
    Does  a max of V passes (worst-case) where a max of E edges are examined in each pass (worst-case) to see if they are eligible to relaxed (and subsequently relaxed if they are eligible).

Note that I implemented this algorithm differently than Sedgewick and Wayne (in a way that is much more intuitive to me).
    I explicitly kept track of the number of "passes" in the algorithm (this is determined by the number of times self.num_rcip reaches 0.
    If the number of "passes" reaches a number greater than V, we know a negative cycle exisits.

    


Example:
python sp_bellmanford.py tinyEWDn.txt ' ' 0
python sp_bellmanford.py tinyEWDnc.txt ' ' 0
python sp_bellmanford.py mediumEWD.txt ' ' 0
python sp_bellmanford.py tinyEWDn.txt ' ' 5

"""

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray
from algorithms_python.chapter_4.edge_weighted_digraphs.directed_edge import Directed_Edge
from algorithms_python.chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList
from algorithms_python.chapter_4.edge_weighted_digraphs.directed_weighted_cycle import Directed_Weighted_Cycle



class Shortest_Paths:
    def __init__(self, ewdg, s):
        self._distTo = [float('inf') for i in range(ewdg.V())]
        self._distTo[s] = 0
        
        self.edgeTo = [None]*ewdg.V()
              
        self.s = s
        
        self.vertex_queue = Queue_LinkedList()
        self.vertex_queue.enqueue(self.s) 
        
        self.on_queue = [False]*ewdg.V()
        self.on_queue[self.s] = True
        
        self.cycle = None
        
        # Keeps track of the number of relax calls that are required in a pass
            # self.num_rcip = self.num_vaip after each pass 
        self.num_rcip = 1
        # Keeps track of the number of edges that were eligible to be relaxed in the pass
        self.num_vaip = 0
        # Keeps track of the number of "passes" in the algorithm
        # When self.num_rcip reaches 0, we know we are starting a new "pass"
        self.pass_count = 1
        
        
        # some way of determining the order methodology of choosing v
            # In this case, we only look at edges coming from vertices that were relaxed in the previous pass instead of all of the edges as in sp_bellmanford_manual.
        print('Pass: ', self.pass_count)
        while self.vertex_queue.isEmpty() == False:
            
            if self.pass_count > ewdg.V():
                print('\n\n Negative cycle is reachable from s. Shortest paths cannot be computed.')
                print('--------------------------------------------------------------------------------- \n\n')
                self.findNegativeCycle()
                return
            
            v = self.vertex_queue.dequeue()
            self.on_queue[v] = False
            
            
            if self.num_rcip == 0:
                self.num_rcip = self.num_vaip
                self.num_vaip = 0
                self.pass_count += 1
                print('\n')
                print('Pass: ', self.pass_count)
            
            
            self.relax(ewdg, v)
            self.num_rcip -= 1
        print('Queue is empty. Shortest paths for all reachable vertices from s have been found.')
        print('--------------------------------------------------------------------------------- \n\n')
        
    
    
    def relax(self, ewdg, v):
        print("from vertex: ",v, " (removed from queue)")
        for edge in ewdg.adjacent(v):
            print('Edge: ', edge)
            v = edge.from_vert()
            w = edge.towards_vert()
            
            if self._distTo[v] + edge.weight() < self._distTo[w]:
                # number of vertices added on this relax
                self.num_vaip += 1
                
                print('This edge is eligible and will be relaxed')
                self.edgeTo[w] = edge
                
                self._distTo[w] = self._distTo[v] + edge.weight()
                print("towards vertex", w)
                if self.on_queue[w] == True:
                    print('The vertex ', w, ' is already on the queue')

                else:
                    print('The vertex ', w, ' was not already on the queue. Added to queue.')
                    self.vertex_queue.enqueue(w)
                    self.on_queue[w] = True
            else:
                print('This edge is ineligible')

            
        
    
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
    
    # This method is not required for the algorithm, I just added this to keep track of the number of "passes"
    def num_passes(self):
        return self.pass_count
        
    def hasNegativeCycle(self):
        return self.cycle != None
        
    def findNegativeCycle(self):
        # Build ew_digraph from edges in edgeTo
        new_graph = Edge_Weighted_Digraph(V=len(self._distTo))
        for edge in self.edgeTo:
            # The entry for self.edgeTo[s] is None
            # Reminder that the 'is' and 'is not' operators test for reference/identity equality
            # In python, there is only one location for None in a python script, no matter how many variables are set to None
            # ie id(edge) == id(None)
            if edge is not None:
                new_graph.addEdge(edge)
        
        # We know there is a (negative) cycle in this ew_digraph    
        cycle_finder = Directed_Weighted_Cycle(new_graph)
        self.cycle = cycle_finder.cycle()
        
    def negativeCycle(self):
        return self.cycle
    
    



def main():
    
    ewdg = Edge_Weighted_Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    source_vertex = int(sys.argv[3])
    sp = Shortest_Paths(ewdg, source_vertex)
    
    if sp.hasNegativeCycle() == False:
        for i in range(ewdg.V()):
            print("Shortest path from ", source_vertex, " to ", i, ":")
            print(sp.pathTo(i))
            print("Total cost:", sp.distTo(i))
            print("\n\n")
        print("Number of passes: ", sp.num_passes())
        
    else:
        print("A negative cycle is reachable from the source vertex.")
        print("Shortest paths could not be found.")
        print("Negative cycle: ")
        print(sp.negativeCycle())

        


if __name__== "__main__": main()