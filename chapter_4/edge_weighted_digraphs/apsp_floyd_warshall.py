
"""
Title: apsp_floyd_washall.py
Author: Ryan Borchardt


Determines the all-paths shortest paths for an edge-weighted digraph (ie determines the shortest paths from every vertex to every other vertex).

Idea: incrementally considering (and building if shorter) all intermediate paths between nodes u and v

# Time complexity: O(V^3)
# Space complexity: O(V^2)

Example:
python apsp_floyd_warshall.py tinyEWDn.txt ' '
"""


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.edge_weighted_digraphs.directed_edge import Directed_Edge
from algorithms_python.chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph



class AP_Shortest_Paths:
    def __init__(self, ewdg):
        V=ewdg.V()
        self.dist_matrix = [[float('inf')]*V for _ in range(V)]
        
        for i in range(V):
            self.dist_matrix[i][i]=0 # shortest distance from any vertex to itself is 0 (assuming no negative cycles)
        
        for edge in ewdg.edges():
            self.dist_matrix[edge.from_vert()][edge.towards_vert()] = edge.weight()
            
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if self.dist_matrix[i][k] + self.dist_matrix[k][j] < self.dist_matrix[i][j]: # if going from i->k->j is shorter than going from i->j, update that distance:
                        self.dist_matrix[i][j] = self.dist_matrix[i][k] + self.dist_matrix[k][j]
            
    
    def shortest_path(self,u,v):
        return self.dist_matrix[u][v]



def main():
    
    ewdg = Edge_Weighted_Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    apsp = AP_Shortest_Paths(ewdg)
    print(apsp.shortest_path(0,5))
    print(apsp.shortest_path(1,2))
        


if __name__== "__main__": main()