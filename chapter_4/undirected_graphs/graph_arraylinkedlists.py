# Title: graph_arraylinkedlists.py
# Author: Ryan Borchardt

# I am implementing the graph data structure using an array of linked lists.
# This is an implementation of the graph API listed on page 522 of Sedgewick and Wayne's Algorithms. 
# This implementation is for: unweighted, undirected graphs that allows for self-loops and parallel edges.
# The names of the vertices are restricted to being integers from 0 to V-1 where V is the number of vertices in the graph.
    # See my alternate implementation (graph_alt.py) that allows for the names of the verticies to be any object. This implementation has additional functionality such as being able to...
# Note that Sedgewick and Wayne implement their graph data strucuture using the Bag data structure that was implemented with linked lists. 

# Note that Sedgewick and Wayne somtimes use the same name for both instance variables and instance methods (for example instance variable self.adj and instance method adj) in their Java code
    # In Python, the instance variable is called self.adj within the class definition and graph.adj in the test client (if the variable graph is a reference to a Graph_ArrayLinkedLists object)
    # The instance method is called self.adj() within the class definition and graph.adj() in the test client
    # This can be problematic in Python b/c: The instance variable will ALWAYS be called when you intend to call the instance method if they share the same name
    # For example, graph.adj(0) in the test client is actually interpreted as applying (0) to the graph.adj instance variable rather than calling the graph.adj() instance method with 0 as an input
    # For clarity, I always make sure that instance variables and instance methods do not share the same name

# Space required: E + V
# Time to add edge v-w: 1
# Time to check whether w is adjacent to v: degree(v)
# Time to iterate through verticies adjacent to v: degree(v)

# Example:
# python graph_arraylinkedlists.py tinyG.txt ' '

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/Ryan/Desktop/Work/')
from algorithms_python.chapter_1.bag.bag_linkedlist import Bag_LinkedList

class Graph_ArrayLinkedLists:
    # Note that in Python, a class can't have more than one constructor (Java allows for more than one constructor).
    # However, Python allows for optional arguments and you can use this to allow for the same functionality 
    def __init__(self, V=None, filename=None, delimiter=None):
        if filename==None:
            self.V = V
            self.E = 0
            self.adj = [Bag_LinkedList()]*self.V
        else:
            # The built-in open() function returns a file object that is iterable (you can iterate through each line of the file object)
            file_object = open(filename, 'r')
    
            # Note that the readline() method consumes the input
            first_line = file_object.readline()
            number_vert = int(first_line)
    
            second_line = file_object.readline()
            number_edge = int(second_line)
            
            self.V = number_vert
            self.E = 0
            # Note that the line of code below that is commented out does NOT work
            # This is b/c each element of the array is a reference to the same Bag_LinkedList object. 
            # This worked for None in the past b/c it doesn't matter if each element in an array referred to the same None object (in those applications)
            #self.adj = [Bag_LinkedList()]*self.V
            # The code below works b/c the list comprehension creates a new (and different) empty Bag_LinkedList object for each element in the array.
            self.adj = [Bag_LinkedList() for i in range(self.V)]
    
            for line_string in file_object:
                # The strip() method for a string object returns a copy of the string where all leading and trailing whitespace are removed from the string (each line_string has the newline '\n' character at the end)
                # The split() method for a string object returns a list object where each element in the list is each segment of the string separated by the specified delimiter
                line_list = line_string.strip().split(delimiter)
                v = int(line_list[0])
                w = int(line_list[1])
                self.addEdge(v,w)
            
      
    def num_V(self):
        return self.V
    
    def num_E(self):
        return self.E
    
    def addEdge(self, v, w):
        # See Bag_LinkedList.py for how we implemented the add() method for Bag_LinkedList objects
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1
    
    # Returns an iterable for the verticies adjacent to v
    def adjacent(self, v):
        # self._adj[v] is a reference to a Bag_LinkedList object
        # for i in Bag_LinkedList object iterates through the items of each node (see how I made Bag_LinkedList object iterable in bag_linkedlist.py)
        return self.adj[v]
    
    def __str__(self):
        returned_string = str(self.V) + ' verticies, ' + str(self.E) + ' edges.' + '\n'
        current_index=0
        for llbag in self.adj:
            # See Bag_LinkedList.py for how we implemented the str() method for Bag_LinkedList objects
            ll_string = str(self.adj[current_index])
            add_string = 'Linked list at index ' + str(current_index) + ': ' + ll_string
            current_index += 1
            returned_string = returned_string + add_string + '\n'
        return returned_string
    
    
def main():
    if len(sys.argv) == 1:
        graph = Graph_ArrayLinkedLists(V=10)
        return
    else:
        filename = sys.argv[1]
        delimiter = sys.argv[2]
        graph = Graph_ArrayLinkedLists(filename=filename, delimiter=delimiter)
        print(graph)
        for i in graph.adjacent(0):
            print(i)
        


if __name__=="__main__": main()
