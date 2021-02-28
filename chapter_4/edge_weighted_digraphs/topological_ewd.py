# Title: topological_ewd.py
# Author: Ryan Borchardt

# topological_ewd.py is adapted from topological.py to allow for determining the dfs orderings of an edge weighted digraph 

# sorts the vertices in a DAG in topological order

# Example:
# python topological_ewd.py tinyEWD.txt ' '
# python topological_ewd.py tinyEWDAG.txt ' '

import sys
from chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph
from chapter_4.edge_weighted_digraphs.directed_weighted_cycle import Directed_Weighted_Cycle
from chapter_4.edge_weighted_digraphs.directed_dfs_orderings_ewd import Directed_DFS_Orderings_EWD

class Topological:
    def __init__(self, ew_digraph):
        if Directed_Weighted_Cycle(ew_digraph).hasCycle()==False:
            self._order = Directed_DFS_Orderings_EWD(ew_digraph).reversepostorder()
        else:
            self._order = None
        
    def order(self):
        return self._order
        
    def isDag(self):
        return self._order != None
        


def main():
    ew_digraph = Edge_Weighted_Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    topological_sort = Topological(ew_digraph)
    
    print('Is DAG?', topological_sort.isDag())
    
    print('Topological Order:')
    print(topological_sort.order())
    
    
if __name__=="__main__": main()