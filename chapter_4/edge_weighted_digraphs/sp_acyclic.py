"""
Title: sp_acyclic.py
Author: Ryan Borchardt

Implementation of API on page 645.

This module required implementing directed_weighted_cycle.py, directed_dfs_orderings_ewd.py and topological_ewd.py 

Advantages over sp_dijkstra:
1. Works for graphs w/ negative weights.
2. Faster run time E*lg(V) vs E+V.

Assumptions:
1. Assumes that the edge-weighted digraph is acyclic.

        
Part of understanding this requires understanding that once a vertex is pulled from the topological sort:
    1. All of the possible paths from the source vertex to this vertex have been examined and
    2. The shortest path has already been selected (this is where the add vertex to the tree operation comes in -> in my case its just a print() statement).

This can be understood by example by looking at the possible paths from Vertex 5 to Vertex 4. 
1. distTo[5] = 0+  Edge(5->4)
2. distTo[5] = 0 + Edge(5->1) + Edge(1->3) + Edge(3->6) + Edge(6->4)

There are no other possible paths. Look at the graph and see for yourself. 

By the time that we pull 4 out of the topological sort we have already looked at all of its dependencies:
1. The Edge(5->4) was eligible and was relaxed.
2. Later on, edge Edge(6->4) was deemed ineligible (b/c 0 + Edge(5->1) + Edge(1->3) + Edge(3->6) + Edge(6->4) was NOT less than 0+  Edge(5->4))

Therefor, by the time we pull 4 out of the topological_sort_stack, we have examined all of the possible paths and have determined the shortest path. 

This is b/c we use topological sort as a methodology for choosing the order of vertices to relax by starting at the vertcies in the order of precedence/prerequisite. By the time we pull a vertex off topological_sort, we have examined the distance of the path to it from all of its dependencies!

Time complexity: Proportional to E + V
    V time to initialize distTo and edgeTo arrays
    E + V time to determine the topological order of the DAG
        E+V time to determine that the directed graph is a DAG
            Uses dfs (E+V time)
        E+V time to determine the dfs orderings (including the reverse postorder)
            Uses dfs (E + V time)
    A vertex is pulled from the topological_order stack V times and relax() is run V times:
        Each call to relax uses  E/V * constant time 
        Overall this is V * E/V * constant time = E time

Space complexity: Proportional to V
    V space for distTo and edgeTo arrays
    V space for the topological order stack
        This uses V space for directed cycle detection
            marked, pathTo, on_stack arrays have length V, cycle_stack has length V
        This uses V space for dfs orderings
            preorder queue, postorder queue, reverse post order stack, marked array all have length V

Example:
python sp_acyclic.py tinyEWDAG.txt ' ' 5

python sp_acyclic.py tinyEWDAG.txt ' ' 1
"""

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray
from algorithms_python.chapter_4.edge_weighted_digraphs.directed_edge import Directed_Edge
from algorithms_python.chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph
from algorithms_python.chapter_4.edge_weighted_digraphs.topological_ewd import Topological


class Shortest_Paths:
    def __init__(self, ewdg, s):
        self._distTo = [float('inf') for i in range(ewdg.V())]
        self._distTo[s] = 0
        
        self.edgeTo = [None]*ewdg.V()
              
        self.s = s
        # some way of determining the order methodology of choosing v:
        topological_order_stack = Topological(ewdg).order()
        print(topological_order_stack)
        

        while topological_order_stack.isEmpty()==False:
            v = topological_order_stack.pop()
            self.relax(ewdg,v)
    
    # vertex or edge relaxation
    def relax(self, ewdg, v):
        print('All the paths from source vertex ', self.s, ' to vertex ', v, ' have been examined and the shortest path has been permanently determined.')
        print("from vertex: ",v)
        for edge in ewdg.adjacent(v):
            print('Edge: ', edge)
            v = edge.from_vert()
            w = edge.towards_vert()
            
            if self._distTo[v] + edge.weight() < self._distTo[w]:
                print('This edge is eligible and will be relaxed')
                self.edgeTo[w] = edge
                
                self._distTo[w] = self._distTo[v] + edge.weight()
                self.edgeTo[w] = edge
                print("towards vertex", w)
            else:
                print('This edge is ineligible')
        print('\n')

            
        
    
    def distTo(self, v):
        return self._distTo[v]
        
    def hasPathTo(self,v):
        return self._distTo[v] != float('inf')
        
    # Returns stack of directed edges from the source vertex s to a given vertex v.    
    def pathTo(self,v):
        if self.hasPathTo(v) == False:
            return None
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