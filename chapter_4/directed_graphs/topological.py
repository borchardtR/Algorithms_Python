# Title: topological.py
# Author: Ryan Borchardt

# sorts the vertices in a DAG in topological order

# Topologically sort a DAG with:
    # Time complexity: Proportional to V + E
    # Space complexity: Proportional to V

# Example:
# python topological.py tinyDAG.txt ' '
# python topological.py tinyDG.txt ' '

import sys

from chapter_4.directed_graphs.digraph import Digraph
from chapter_4.directed_graphs.directed_cycle import Directed_Cycle
from chapter_4.directed_graphs.directed_dfs_orderings import Directed_DFS_Orderings

class Topological:
    def __init__(self, digraph):
        if not Directed_Cycle(digraph).hasCycle():
            self._order = Directed_DFS_Orderings(digraph).reversepostorder()
        else:
            self._order = None
        
    def order(self):
        return self._order
        
    def isDag(self):
        return self._order is not None
        


def main():
    digraph = Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    topological_sort = Topological(digraph)
    
    print('Is DAG?', topological_sort.isDag())
    
    print('Topological Order:')
    print(topological_sort.order())
    
    
if __name__=="__main__": main()