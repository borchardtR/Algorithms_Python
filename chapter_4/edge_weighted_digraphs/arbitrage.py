"""
Title: arbitrage.py
Author: Ryan Borchardt

This algorithm uses an edge_weighted_digraph and a negative cycle detection (in this case shortest path Bellman Ford) algorithm to identify arbitrage opporunties from a table of currencies and their exchange rates.    

It doesn't guarantee to find the best arbitrage opportunity, just a arbitrage opportunity that is profitable.

To find the best arbitrage opportunity, could implement an algorithm that takes ln() of each exchange rate and DOESN'T negate it as the edge weights in an edge weighted digraph.
    Would then be reduced to a longest cycle path problem. 

# Example:
# python arbitrage.py rates.txt ' '
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
    
    name_list = []
    
    for i in range(num_verts):
        list_string = file_object.readline().strip().split()
        print(list_string)
        name_list.append(list_string[0])
        for j in range(1,num_verts+1):
            if i != (j-1):
                edge_weight = math.log(float(list_string[j]))*-1
                directed_edge = Directed_Edge(v=i, w=j-1, weight=edge_weight)
                ewdag.addEdge(directed_edge)
    return (ewdag, name_list)
    
def find_negative_cycle(ewdag, name_list):
    stake = 1000
    sp = Shortest_Paths(ewdag,0)
    if sp.hasNegativeCycle() == True:
        print('Arbitrage opporunity identified:')
        neg_cycle = sp.negativeCycle()
        for edge in neg_cycle:
            conversion = math.exp((edge.weight()*-1))
            new_amount = conversion*stake
            print(stake, name_list[edge.from_vert()], ' to ', new_amount, name_list[edge.towards_vert()])
            stake = new_amount
    else:
        print('No arbitrage opporunity identified:')
    
        
def main():
    ewdag, name_list = build_ewdag(sys.argv[1], sys.argv[2])
    find_negative_cycle(ewdag, name_list)
    
    

if __name__=="__main__": main()