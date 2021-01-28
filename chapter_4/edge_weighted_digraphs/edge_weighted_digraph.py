"""
Title: edge_weighted_digraph.py
Author: Ryan Borchardt

This implements an edge-weighted digraph using an array of linked lists where the nodes in each linked list contain references to Directed edge objects 
The implementation is very similar to edge_weighted_graph.py except for a given vertex and its corresponding element in the array, 
    its linked list only contains references to directed edge objects that point FROM the vertex (rather than all edges connected to that vertex).
Each element in the array corresponds to a vertex and each of its elements contains a reference linked list where all of the edges from that particular vertex are listed.
Each node in a linked list contains a reference to a Directed_Edge object (in the node's self.item instance variable).


Example:
python edge_weighted_digraph.py tinyEWD.txt ' '

"""

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_1.bag.bag_linkedlist import Bag_LinkedList
from algorithms_python.chapter_4.edge_weighted_digraphs.directed_edge import Directed_Edge



class Edge_Weighted_Digraph:
    def __init__(self, V=None, filename=None, delimiter=None):
        if V is not None:
            self._V= V
            self._E = 0
            self.adj = [Bag_LinkedList() for i in range(self._V)]
        
        if filename is not None:
            file_object = open(filename, 'r')
            self._V = int(file_object.readline())
            # I prefer to dynamically determine _E
            # consuming the line that contains the # of edges
            file_object.readline()
            self._E = 0
            
            self.adj = [Bag_LinkedList() for _ in range(self._V)]
        
            for line in file_object:
                line = line.strip().split()
                vertex_from = int(line[0])
                vertex_towards = int(line[1])
                weight = float(line[2])
                directed_edge = Directed_Edge(vertex_from, vertex_towards, weight)
                self.addEdge(directed_edge)
                
    
    def V(self):
        return self._V
        
    def E(self):
        return self._E
    
    def addEdge(self, directed_edge):
        v = directed_edge.from_vert()
        w = directed_edge.towards_vert()
        
        # Edge is only added to linked list of vertex that the edge is pointing from
        self.adj[v].add(directed_edge)
        self._E += 1
    
    # Returns an iterable of edges directed from a given vertex, v (as a bag of edges)
    def adjacent(self, v):
        return self.adj[v]
    
    # returns iterable of all edges
    def edges(self):
        iterable_edges = Bag_LinkedList()
        for linked_list in self.adj:
            for item in linked_list:
                iterable_edges.add(item)
        return iterable_edges
                

           
            
    def __str__(self):
        string = ""
        for i in range(self.V()):
            string = string + 'Edges coming from vertex ' +str(i) + ':' + '\n' + str(self.adjacent(i)) + '\n\n'
        return string



def main():
    
    ewdg = Edge_Weighted_Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    print(ewdg.V())
    print(ewdg.E())
    print(ewdg)
    
    for i in ewdg.edges():
        print(i)
        


if __name__=="__main__": main()