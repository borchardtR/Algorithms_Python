# Title: symbol_graph.py
# Author: Ryan Borchardt

# The Symbol_Graph serves as a sort of "skin" for the Graph_Array_AdjacencyLists structure.
    # It allows the vertices of a graph to be labeled anything and not be restricted to names that are 0...graph.V()
    # It doesn't change the space complexity of the graph:
        # The additional instance variable, st, takes space proportional to V
        # The additional instance variable, inverted_index, takes space proprotional to V.
        # The graph takes space proprotional to V+E, so the overall space complexity of the graph remains the same.
    # It doesn't change the time complexity of any of the graph operations:
        # The methods contains(), index(), name(), G() all add constant time to each of their respective operations so the overall time complexity of the graph operations remain the same.    


# I am implementing the graph data structure using a symbol table.
# Important note: This data strucuture builds off and uses the graph_array_adjacencylists structure.
# The Symbol_Graph has three main instance variables:
# 1. self.st is a symbol table where the keys are the names of the verticies and their corresponding values are their integer counterparts between 0 to V-1 (this allows us to incorporate the graph_array_adjacencylists structure seamlessly).
# 2. self.graph is the graph_array_adjacencylists structure where the adjacent verticies are stored as their integer index equivalents in a linked list stored at the index of the array corresponding to the given vertex.
# 3. self.inverted_index allows for looking up the string name of a vertex given its integer index value. It serves the opposite function of looking up a key in self.st.

# This extends the functionality to allow for vertices with string names rather than integers from 0 to V-1.

# This is an implementation of the graph API listed on page 548 of Sedgewick and Wayne's Algorithms. 
# This implementation is for: unweighted, undirected graphs that allows for self-loops and parallel edges.


# Note that Sedgewick and Wayne somtimes use the same name for both instance variables and instance methods (for example instance variable self.adj and instance method adj) in their Java code
    # In Python, the instance variable is called self.adj within the class definition and graph.adj in the test client (if the variable graph is a reference to a Graph_Array_AdjacencyLists object)
    # The instance method is called self.adj() within the class definition and graph.adj() in the test client
    # This can be problematic in Python b/c: The instance variable will ALWAYS be called when you intend to call the instance method if they share the same name
    # For example, graph.adj(0) in the test client is actually interpreted as applying (0) to the graph.adj instance variable rather than calling the graph.adj() instance method with 0 as an input
    # For clarity, I always make sure that instance variables and instance methods do not share the same name

# The performance of the Symbol_Graph is similar to Graph_Array_AdjacencyLists simply b/c:
    # Symbol_Graph builds off and uses Graph_Array_AdjacencyLists 
    # The only additional operations come from the symbol table and inverted index array.
    # All of the operations used are constant for the symbol table and constant (constant amortized when appending) for the inverted_index array. 
    
# The Symbol_Graph data structure requires slightly more space than the Graph_Array_AdjacencyLists but is still on the same scale:
    # The Symbol_Graph has two additional instance variables: an array of length V and a symbol table with V key:value pairs
    # The space required is still proportional to E + V

# Space required: E + V
# Time to add edge v-w: 1
# Time to check whether w is adjacent to v: degree(V) + other constant-time operations
# Time to iterate through verticies adjacent to v: degree(V) + other constant-time operations

# Example:
# python symbol_graph.py routes.txt ' '
# python symbol_graph.py movies.txt '/'

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.undirected_graphs.graph_array_adjacencylists import Graph_Array_AdjacencyLists
from algorithms_python.chapter_3.st_hashtable_separatechaining.st_hashtable_separatechaining import ST_HashTable_SeparateChaining

class Symbol_Graph:
    def __init__(self, filename, delimiter):
        self.st = ST_HashTable_SeparateChaining()
        self.inverted_index = []
        
        
        file_object = open(filename, 'r', encoding='utf-8')
        index_count = 0
        
        for line in file_object:
            line_list = line.strip().split(delimiter)
            for vertex in line_list:
                if not self.st.contains(vertex):
                    self.st.put(vertex,index_count)
                    self.inverted_index.append(vertex)
                    index_count+=1
        file_object.close()
         
        
        self.graph = Graph_Array_AdjacencyLists(V=index_count)
        
        file_object = open(filename, 'r', encoding='utf-8')
        
        for line in file_object:
            line_list = line.strip().split(delimiter)
            first_vertex_int = self.st.get(line_list[0])
            for i in range(1,len(line_list)):
                next_vertex = self.st.get(line_list[i])
                self.graph.addEdge(first_vertex_int, next_vertex)
        file_object.close()
        
        
            
    
    def contains(self, key):
        return self.st.get(key) is not None
    
    def index(self, key):
        return self.st.get(key)
    
    def name(self, int):
        return self.inverted_index[int]
        
    def G(self):
        return self.graph
        
    def __str__(self):
        returned_string = str(self.graph._V) + ' verticies, ' + str(self.graph._E) + ' edges.' + '\n'
        current_index=0
        for llbag in self.graph.adj:
            ll = self.graph.adj[current_index]
            add_string = 'Verticies adjacent to ' + str(self.inverted_index[current_index]) + ': '
            for node in ll:
                if node is not None:
                    add_string = add_string + str(self.inverted_index[node]) + ', '
            current_index += 1
            returned_string = returned_string + add_string[:len(add_string)-2] + '\n'
        return returned_string
    
        

def main():
    sg = Symbol_Graph(filename=sys.argv[1], delimiter=sys.argv[2])
    print(sg)


if __name__=="__main__": main()





