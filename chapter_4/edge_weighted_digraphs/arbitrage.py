"""
Title: arbitrage.py
Author: Ryan Borchardt
    


# Example:
# python arbitrage.py rates.txt ' '
#
"""

import sys
import math
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.edge_weighted_digraphs.directed_edge import Directed_Edge
from algorithms_python.chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph
from algorithms_python.chapter_4.edge_weighted_digraphs.sp_bellmanford import Shortest_Paths



def build_ewdag(filename, delimter):
    file_object = open(filename, 'r')
    
    num_verts = int(file_object.readline())
    
    ewdag = Edge_Weighted_Digraph(num_verts)
    
    
    
    for i in range(num_verts):
        list_string = file_object.readline().strip().split()
        print(list_string)
        for j in range(1,num_verts+1):
            if i != (j-1):
                edge_weight = math.log(float(list_string[j]))*-1
                directed_edge = Directed_Edge(v=i, w=j-1, weight=edge_weight)
                ewdag.addEdge(directed_edge)
    return ewdag
    
def find_negative_cycle(ewdag):
    stake = 1000
    sp = Shortest_Paths(ewdag,0)
    if sp.hasNegativeCycle() == True:
        print('Arbitrage opporunity identified:')
        neg_cycle_stack = sp.negativeCycle()
        while neg_cycle_stack.isEmpty()+=False:
            vertex_from = neg_cycle_stack.pop()
            vertex_to = neg_cycle_stack.pop()
            for edge in ewdag.adjacent(vertex_from):
                if edge.towards_vert() == vertex_to:
                  
                conversion = math.exp((edge.weight()*-1))
                new_amount = conversion*stake
                print(stake, edge.from_vert(), ' to ', new_amount, edge.towards_vert())
                stake = new_amount
            
    else:
        print('No arbitrage opporunity identified:')
    
        
def main():
    ewdag = build_ewdag(sys.argv[1], sys.argv[2])
    find_negative_cycle(ewdag)
    
    

if __name__=="__main__": main()