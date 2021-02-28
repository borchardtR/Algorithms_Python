"""
Title: lp_acyclic.py
Author: Ryan Borchardt

This module extends the functionality of edge weighted digraphs to be able to determine the longest paths from a source vertex to all other vertices.
The implementation of this module is exactly the same as the shortest path acyclic module (sp_acyclic.py) except: 
    1. the distTo values are initialized to negative infinity instead of positive infinity
    2. An edge (v->w) is eligible to be relaxed if self._distTo[v] + edge.weight() > self._distTo[w] (switched the signs around)

Note that there is an alternative to this implementation presented in the book:
    1. Create a copy of the edge weighted digraph where all of the weights are negated
    2. Find the shortest paths using sp_acyclic.py (these are the longest paths in the original graph)
    3. When returning total weight of the paths, negate each of the total weights

Assumptions:
1. Assumes that the edge-weighted digraph is acyclic.
2. Requires that we know the vertex with highest precedence order (as the source vertex) in the acyclic weighted digraph.

Takes space proportional to V.

Takes time proportional to E+V.
    Involves doing a topogological sort of the ewdg:
        cycle detection (directed_weighted_cycle.py) uses dfs which takes time proprotional to E+V.
        getting the reverse postorder (directed_dfs_orderings_ewd.py) uses dfs which takes time proprotional to E+V.
    Involves a call to relax() for each vertex. At each vertex, relax does the following: (this sums to E+V run time)
        Add vertex to the tree (which in my case is a simple print('The longest path has been determined for vertex v') statement), (this is done V*1 = V total times) 
        Iterate through adjacency list and do a series of constant time operations (this is done V*(num_neighbors(V)*1) = E total time)
        
        
Part of understanding this requires understanding that once a vertex is called from the topological sort, its longest path has already been determined (this is where the add vertex to the tree operation comes in -> in my case its just a print() statement).

This can be understood by example by looking at the possible paths from Vertex 5 to Vertex 4. 
1. distTo[5] = 0+  Edge(5->4)
2. distTo[5] = 0 + Edge(5->1) + Edge(1->3) + Edge(3->6) + Edge(6->4)

There are no other possible paths. Look at the graph and see for yourself. 

By the time that we pull 4 out of the topological sort we have already looked at all of its dependencies:
1. The Edge(5->4) was eligible and was relaxed.
2. Later on, edge Edge(6->4) was deemed eligible and relaxed (and distTo[4] is updated to this larger value): (b/c 0 + Edge(5->1) + Edge(1->3) + Edge(3->6) + Edge(6->4) was greater than than 0+  Edge(5->4))

Therefor, by the time we pull 4 out of the topological_sort_stack, we have examined all of the possible paths and have determined the longest path. 

This is b/c we use topological sort as a methodology for choosing the order of vertices to relax by starting at the vertcies in the order of precedence/prerequisite. By the time we pull a vertex off topological_sort, we have examined the distance of the path to it from all of its dependencies!


Example:
python lp_acyclic.py tinyEWDAG.txt ' ' 5
python lp_acyclic.py tinyEWDAG.txt ' ' 4
"""

import sys

from chapter_1.stack.stack_resizingarray import Stack_ResizingArray
from chapter_4.edge_weighted_digraphs.directed_edge import Directed_Edge
from chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph
from chapter_4.edge_weighted_digraphs.topological_ewd import Topological


class Longest_Paths:
    def __init__(self, ewdg, s):
        self._distTo = [float('-inf') for i in range(ewdg.V())]
        self._distTo[s] = 0
        
        self.edgeTo = [None]*ewdg.V()
              
        self.s = s
        # some way of determining the order methodology of choosing v:
        topological_order_stack = Topological(ewdg).order()
        print(topological_order_stack)
        

        while topological_order_stack.isEmpty()==False:
            v = topological_order_stack.pop()
            self.relax(ewdg,v)
    
    # vertex relaxation =( E/V edge relaxation)
    def relax(self, ewdg, v):
        print('The longest path to vertex ', v, 'has been permanently determined.')
        print("from vertex: ",v)
        for edge in ewdg.adjacent(v):
            print('Edge: ', edge)
            v = edge.from_vert()
            w = edge.towards_vert()
            
            if self._distTo[v] + edge.weight() > self._distTo[w]:
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
        return self._distTo[v] != float('-inf')
        
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
    lp = Longest_Paths(ewdg, source_vertex)
    print(lp._distTo)
    
    for i in range(ewdg.V()):
        print("Longest path from ", source_vertex, " to ", i, ":")
        print(lp.pathTo(i))
        print("Total cost:", lp.distTo(i))
        print("\n\n")

        


if __name__== "__main__": main()