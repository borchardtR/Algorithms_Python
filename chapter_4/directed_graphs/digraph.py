# Title: digraph.py
# Author: Ryan Borchardt

# The implementation for the digraph data structure is very similar to the implementation for the (undirected graph) Graph_Array_AdjacencyLists.

# Constructing the digraph:
    # Time complexity: Proportional to V + E 
        # 1. Build self.adj which consists of an array of V empty linked lists (time proportional to V)
        # 2. For each edge, add an integer to a specific linked list (time proportional to E)
    # Space complexity: Proportional to V + E
        # The self.adj instance variabe is an array of length V. It contains V references to V linked lists.
        # The average length of the linked lists is equal to the average outdegree (# of edges pointing from a vertex) per vertex: E / V. So the sum of all of the linked lists take V * E /V = E space 
        # So the overall space taken is V references to V lists and E total nodes.
    
# Reminder that for a digraph, the average outdegree per vertex = E / V.
    # For an undirected graph, the average degree per vertex = 2E / V.


# Example:
# python digraph.py tinyDG.txt ' '


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_1.bag.bag_linkedlist import Bag_LinkedList

class Digraph:
    # Note that the code for the constructor of the Digraph data type is the same as that for the undirected graph (Graph_Array_AdjacencyLists).
    # Note that in Python, a class can't have more than one constructor (Java allows for more than one constructor).
    # However, Python allows for optional arguments and you can use this to allow for the same functionality 
    def __init__(self, V=None, filename=None, delimiter=None):
        if filename==None:
            self._V = V
            self._E = 0
            self.adj = [Bag_LinkedList() for i in range(self._V)]
        else:
            # The built-in open() function returns a file object that is iterable (you can iterate through each line of the file object)
            file_object = open(filename, 'r')
    
            # Note that the readline() method consumes the input
            first_line = file_object.readline()
            number_vert = int(first_line)
    
            second_line = file_object.readline()
            number_edge = int(second_line)
            
            self._V = number_vert
            self._E = 0
            # Note that the line of code below that is commented out does NOT work
            # This is b/c each element of the array is a reference to the same Bag_LinkedList object. 
            # This worked for None in the past b/c it doesn't matter if each element in an array referred to the same None object (in those applications)
            #self.adj = [Bag_LinkedList()]*self._V
            # The code below works b/c the list comprehension creates a new (and different) empty Bag_LinkedList object for each element in the array.
            self.adj = [Bag_LinkedList() for i in range(self._V)]
    
            for line_string in file_object:
                # The strip() method for a string object returns a copy of the string where all leading and trailing whitespace are removed from the string (each line_string has the newline '\n' character at the end)
                # The split() method for a string object returns a list object where each element in the list is each segment of the string separated by the specified delimiter
                # The default delimiter is whitespace
                line_list = line_string.strip().split()
                v = int(line_list[0])
                w = int(line_list[1])
                self.addEdge(v,w)
    
    def V(self):
        return self._V
    
    def E(self):
        return self._E
    
    def addEdge(self, v, w):
        self.adj[v].add(w)
        self._E+=1
    
    def adjacent(self, v):
        return self.adj[v]
    
    # Returns a digraph object where the edges are all reversed
    # Allows client to efficiently find edges pointing TOWARDS a given vertex
    def reverse(self):
        rev_digraph = Digraph(V=self._V)
        for from_vert in range(len(self.adj)):
            for toward_vert in self.adj[from_vert]:
                rev_digraph.addEdge(toward_vert, from_vert)
        return rev_digraph
    
    def __str__(self):
        string = ''
        for i in range(len(self.adj)):
            string = string + "Vertex " + str(i) + " points towards: "
            for node in self.adj[i]:
                string = string + str(node) + ", "
            string = string + "\n"
        return string


def main():
    digraph = Digraph(filename=sys.argv[1], delimiter=sys.argv[2])
    print('Digraph:')
    print(digraph)


    digraph_reversed = digraph.reverse()
    print('Reversed digraph:')
    print(digraph_reversed)
if __name__=="__main__": main()