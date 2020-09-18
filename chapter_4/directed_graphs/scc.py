# Title: scc_quadratic.py
# Author: Ryan Borchardt

# Identifies the strongly connected components in a directed graph

# This implementation takes quadratic time:
    # Creates a Paths_DFS_Directed data structure for each vertex (V*(V+E))
    # Uses two nested for loops to see if there is a path from vertex i to vertex j (V^2 * constant time)
    # This implementation takes time proportional to V^2 + V*E


# Example:
# python scc.py tinyDG.txt ' '
# python scc.py tinyDG_other.txt ' '
# python scc.py tinyDAG.txt ' '

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.directed_graphs.digraph import Digraph
from algorithms_python.chapter_4.directed_graphs.directed_cycle import Directed_Cycle
from algorithms_python.chapter_4.directed_graphs.directed_dfs_orderings import Directed_DFS_Orderings
from algorithms_python.chapter_4.directed_graphs.paths_dfs_directed import Paths_DFS_Directed


class SCC:
    def __init__(self, digraph):
        self.scc_id = [None]*digraph.num_V()
        self.paths_array = []
        self.scc_count = -1
        
        for i in range(digraph.num_V()):
            self.paths_array.append(Paths_DFS_Directed(digraph,i))
        
        for i in range(digraph.num_V()):
            if self.scc_id[i] == None:
                self.scc_count += 1
                print('New component', i)
                self.scc_id[i] = self.scc_count
                for j in range(digraph.num_V()):
                    # If this is true, then vertices i and j are strongly connected.
                    if (self.scc_id[j] == None) and (i!=j):
                        if self.paths_array[i].hasPathTo(j) and self.paths_array[j].hasPathTo(i):
                            print(i, j, 'strongly connected')
                            self.scc_id[j] = self.scc_count

        
    def stronglyConnected(self, v, w):
        return self.scc_id[v] == self.scc_id[w]
        
    def count(self):
        return self.scc_count+1
    
    def id(self, v):
        return self.scc_id[v]
        


def main():
    digraph = Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    scc = SCC(digraph)
    
    print(scc.scc_id)
    
    print(scc.stronglyConnected(0,5))
    print(scc.stronglyConnected(0,8))
    
    print(scc.count())
    
    print(scc.id(0))
    print(scc.id(5))
    print(scc.id(8))
    
    
if __name__=="__main__": main()