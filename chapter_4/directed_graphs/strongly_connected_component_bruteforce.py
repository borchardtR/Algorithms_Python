# Title: scc_bruteforce.py
# Author: Ryan Borchardt


# Example:
# python scc_bruteforce.py tinyDG.txt ' '
# python scc_bruteforce.py tinyDG_other.txt ' '
# python scc_bruteforce.py tinyDAG.txt ' '

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.directed_graphs.digraph import Digraph
from algorithms_python.chapter_4.directed_graphs.directed_dfs import Directed_DFS


class SCC:
    def __init__(self, digraph):
        
        self.component_number = -1
        self.component_id_array = [None]*digraph.V()
        
        # This object is an array of length V with V references to directed_DFS objects of length V.
        # ie this object will take space proportional to V^2
        self.marked_matrix = [None]*digraph.V()
        
        # builds the marked_matrix by building a Directed_DFS object V times
            # building a single Directed_DFS object takes V+E time (using dfs algorithm)
            # so building the marked_matrix takes time proportional to V(V+E)
        for i in range(digraph.V()):
            sself.marked_matrix[i] = Directed_DFS(digraph, i)
        
        # This takes a maximum time of V^2
        for i in range(digraph.V()):
            if self.component_id_array[i] == None:
                self.component_number += 1
                self.component_id_array[i] = self.component_number
                for j in range(digraph.V()):
                    if self.marked_matrix[i].marked_array[j] == self.marked_matrix[j].marked_array[i]:
                        self.component_id_array[j] = self.component_number
                    
    def stronglyConnected(self, v, w):
            return self.component_id_array[v] == self.component_id_array[w]
    
    def count(self):
        return self.component_number + 1
    
    def id(self, v):
        return self.component_id_array[v] 
        



def main():
    digraph = Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    
    scc = SCC(digraph)
    
    print(scc.component_id_array)
    
    print(scc.stronglyConnected(0,5))
    print(scc.stronglyConnected(0,8))
    
    print(scc.count())
    
    print(scc.id(0))
    print(scc.id(5))
    print(scc.id(8))
    
if __name__=="__main__": main()