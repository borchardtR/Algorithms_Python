# Title: degrees_of_separation.py
# Author: Ryan Borchardt

# This module uses the Symbol_Graph, Paths_bfs, and Biparite data structures to determine the degrees of separation between two vertices (the length of the shortest path between two vertices).


# Example:
# python degrees_of_separation.py routes.txt ' ' JFK LAS
# python degrees_of_separation.py movies.txt '/' 'Bacon, Kevin' 'Hanks, Tom'
# python degrees_of_separation.py movies.txt '/' 'Bacon, Kevin' 'Kidman, Nicole'

import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.undirected_graphs.symbol_graph import Symbol_Graph
from algorithms_python.chapter_4.undirected_graphs.paths_bfs import Paths_bfs
from algorithms_python.chapter_4.undirected_graphs.biparite_bfs import Biparite

def main():
    sg = Symbol_Graph(filename=sys.argv[1], delimiter=sys.argv[2])
    vertex_1_int = sg.index(sys.argv[3])
    vertex_2_int = sg.index(sys.argv[4])
    shortest_paths = Paths_bfs(graph=sg.G(), s=vertex_1_int)
    shortest_path_stack = shortest_paths.pathTo(vertex_2_int)
    dos = len(shortest_path_stack)-1
    
    path_string = ''
    for vertex_int in shortest_path_stack:
        if vertex_int == vertex_2_int:
            vertex = sg.name(vertex_int)
            path_string = path_string + vertex
        else:
            vertex = sg.name(vertex_int)
            path_string = path_string + vertex + ' -> '
    print('Shortest path from ', sys.argv[3], "to ", sys.argv[4], ":", path_string)    
    
    
    # If the graph is biparite, the degrees of separation is half of what is initially calculated
    bp = Biparite(sg.G())
    
    if not bp.isBiparite():
        print("Degrees of separation between ", sys.argv[3], "and ", sys.argv[4], ": ", dos) 
    else: 
        print("Degrees of separation between ", sys.argv[3], "and ", sys.argv[4], ": ", dos//2)
if __name__ == "__main__": main()