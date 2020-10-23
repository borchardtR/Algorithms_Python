# Title: edge_weighted_graph.py
# Author: Ryan Borchardt

# This implements an edge-weighted (undirected) graph using an array of linked lists where the nodes in each linked list contain references to Edge objects 
# The implementation is very similar to graph_array_adjacencylists.py except instead of the node's self.item instance variable being a reference to an int object (vertex), it is a reference to an Edge object.
# Each element in the array corresponds to a vertex and each of its elements contains a reference linked list where all of the edges connected to that particular vertex are listed.
# Each node in a linked list contains a reference to an Edge object (in the node's self.item instance variable).


# Example:
# python edge_weighted_graph.py tinyEWG.txt ' '


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_1.bag.bag_linkedlist import Bag_LinkedList
from algorithms_python.chapter_4.edge_weighted_graphs.edge import Edge



class Edge_Weighted_Graph:
    def __init__(self, V=None, filename=None, delimiter=None):
        if V!=None:
            self._V= V
            self._E = 0
            self.adj = [Bag_LinkedList() for i in range(self._V)]
        
        if filename != None:
            file_object = open(filename, 'r')
            self._V = int(file_object.readline())
            # I prefer to dynamically determine _E
            # consuming the line that contains the # of edges
            file_object.readline()
            self._E = 0
            
            self.adj = [Bag_LinkedList() for i in range(self._V)]
        
            for line in file_object:
                line = line.strip().split()
                vertex_1 = int(line[0])
                vertex_2 = int(line[1])
                weight = float(line[2])
                edge = Edge(vertex_1, vertex_2, weight)
                self.addEdge(edge)
                
    
    def V(self):
        return self._V
        
    def E(self):
        return self._E
    
    def addEdge(self, edge):
        v = edge.either()
        w = edge.other(v)
        
        
        self.adj[v].add(edge)
        self.adj[w].add(edge)
        self._E += 1
    
    # Returns an iterable of edges connected a given vertex, v (as a bag of edges)
    def adjacent(self, v):
        return self.adj[v]
    
    # returns iterable of all edges (as a bag of unique edges)
    def edges(self):
        # 1. if using edge_array, takes quadratic time: E*(V+E) 
        # edge_array = []
        
        # 2. use set instead to reduce time to linear time: constant*(V+E)
        #    Python's built-in set data structure
        
        
        # edge_set = ST_HashTable_SeparateChaining()
        # for linked_list in self.adj:
        #     for edge in linked_list:
        #         if edge not in edge_set:
        #             edge_set.add(edge)
        # return edge_set
    
        #3. The implementation provided in the book: takes linear time (V+E)
        # only adds each edge once b/c only adds for when vertex with lower label is iterated through
        bag_unique_edges = Bag_LinkedList()
        for v in range(self.V()):
             for edge in self.adjacent(v):
                 if edge.other(v) > v:
                     bag_unique_edges.add(edge)
        return bag_unique_edges
           
            
    def __str__(self):
        string = ""
        for i in range(self.V()):
            string = string + 'Edges connected to vertex ' +str(i) + ':' + '\n' + str(self.adjacent(i)) + '\n\n'
        return string



def main():
    
    ewg = Edge_Weighted_Graph(filename=sys.argv[1], delimiter=sys.argv[2])
    print(ewg.V())
    print(ewg.E())
    print(ewg)
    
    for i in ewg.edges():
        print(i)
        


if __name__=="__main__": main()