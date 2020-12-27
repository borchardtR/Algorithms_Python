In this side project, I am constructing all of the algorithms listed in Sedgewick and Wayne's 'Algorithms' in Python. 
The algorithms in Sedgewick and Wayne's 'Algorithms' are written in Java. 

My goals for this project are:
1. To increase my understanding of the fundamental data structures and algorithms. 
2. To better understand the underlying mechanisms of object-oriented programing in Python by comparing and contrasting it with Java.

## Table of Contents:

### Chapter 1
- #### Stack<br>
  - [Stack implemented with resizing array](chapter_1/stack/stack_resizingarray.py)<br>
  - [Stack implemented with fixed to resizing array](chapter_1/stack/stack_resizingarray.py)<br>
  - [Stack implemented with linked list](chapter_1/stack/stack_resizingarray.py)<br>
- #### Queue<br>
  - [Queue implemented with linked list](chapter_1/queue/queue_linkedlist.py)<br>
- #### Bag<br>
  - [Bag implemented with linked list](chapter_1/bag/bag_linkedlist.py)<br>
- #### Union Find<br>
  - [Union Quick Find](chapter_1/union_find/uf_quickfind.py)<br>  
  - [Union Quick Union](chapter_1/union_find/uf_quickunion.py)<br>
  - [Union Weighted Quick Union](chapter_1/union_find/uf_weightedquickunion.py)<br>  
  - [Union Weighted Quick Union with path compression](chapter_1/union_find/uf_weightedquickunion_pathcompression.py)<br>

  
### Chapter 2
- #### [Selection sort](chapter_2/selection_sort/selection_sort.py)<br>
- #### [Insertion sort](chapter_2/insertion_sort/insertion_sort.py)<br>
- #### Shell sort<br>
  - [Shell sort basic](chapter_2/shell_sort/shell_sort.py)<br>
  - [Shell sort with detailed explanation](chapter_2/shell_sort/shell_sort_explanation.py)<br>
- #### [Merge sort (recursive)](chapter_2/merge_sort/mergesort_recursive.py)<br>
- #### [Merge sort (iterative)](chapter_2/merge_sort/mergesort_iterative.py)<br>
- #### [Quicksort](chapter_2/quicksort/quicksort.py)<br>
- #### [Heapsort](chapter_2/heapsort/heapsort.py)<br>
- #### Priority Queue<br>
  - [Priority queue (max) implemented with unordered array](chapter_2/priority_queue/priorityqueue_unorderedarray.py)<br>
  - [Priority queue (max) implemented with ordered array](chapter_2/priority_queue/priorityqueue_orderedarray.py)<br>
  - [Priority queue (max) implemented with unordered linked list](chapter_2/priority_queue/priorityqueue_unorderedlinkedlist.py)<br>
  - [Priority queue (max) implemented with ordered linked list](chapter_2/priority_queue/priorityqueue_orderedlinkedlist.py)<br>
  - [Priority queue (max) implemented with binary heap](chapter_2/priority_queue/priorityqueue_binaryheap.py)<br>
  - [Priority queue (min) implemented with binary heap](chapter_2/priority_queue/priorityqueue_min_binaryheap.py)<br>  
  
- #### Indexed Priority Queue<br>
  - [(Standard) Indexed (min) priority queue implemented with binary heap](chapter_2/priority_queue/indexed_priorityqueue_min_standard.py)<br>  
  - [(Custom) Indexed (min) priority queue implemented with binary heap](chapter_2/priority_queue/indexed_priorityqueue_min_custom.py)<br>   
### Chapter 3
- #### Symbol Table<br>
  - [Symbol table implemented with unordered linked list](chapter_3/st_sequentialsearch_unorderedlinkedlist/st_sequentialsearch_unorderedlinkedlist.py)<br>
  - [Symbol table implemented with ordered array](chapter_3/st_binarysearch_orderedarray/st_binarysearch_orderedarray.py)<br>
  - [Symbol table implemented with binary search tree](chapter_3/st_binarysearchtree/st_binarysearchtree.py)<br>
  - [Symbol table implemented with red-black binary search tree](chapter_3/st_redblack_binarysearchtree/st_redblack_binarysearchtree.py)<br>
  - [Symbol table implemented with hash table using separate chaining](chapter_3/st_hashtable_separatechaining/st_hashtable_separatechaining.py)<br>
  - [Symbol table implemented with hash table using linear probing](chapter_3/st_hashtable_linearprobing/st_hashtable_linearprobing.py)<br>
  
  ### Chapter 4
- #### Undirected Graphs<br>
  - [Undirected graph implemented with array of linked lists](chapter_4/undirected_graphs/graph_array_adjacencylists.py)<br>
  - [Depth first search (recursive)](chapter_4/undirected_graphs/dfs_recursive.py)<br>
  - [Depth first search (iterative)](chapter_4/undirected_graphs/dfs_iterative.py)<br>
  - [Path detection DFS (recursive)](chapter_4/undirected_graphs/paths_dfs_recursive.py)<br>
  - [Path detection DFS (iterative)](chapter_4/undirected_graphs/paths_dfs_iterative.py)<br>
  - [Path detection BFS](chapter_4/undirected_graphs/paths_bfs.py)<br>
  - [Connected component detection DFS](chapter_4/undirected_graphs/connected_components.py)<br>
  - [Connected component detection BFS](chapter_4/undirected_graphs/connected_components_bfs.py)<br>
  - [Cycle detection DFS](chapter_4/undirected_graphs/cycle.py)<br>
  - [Cycle detection BFS](chapter_4/undirected_graphs/cycle_bfs.py)<br>
  - [Biparite detection DFS](chapter_4/undirected_graphs/biparite.py)<br>
  - [Biparite detection BFS](chapter_4/undirected_graphs/biparite_bfs.py)<br>
  - [Undirected graph implemented with symbol table](chapter_4/undirected_graphs/symbol_graph.py)<br>
  - [Degrees of separation](chapter_4/undirected_graphs/degrees_of_separation.py)<br>
  
- #### Directed Graphs <br>
  - [Digraph](chapter_4/directed_graphs/digraph.py)<br>
  - [Directed depth first search (recursive)](chapter_4/directed_graphs/directed_dfs.py)<br>
  - [Path detection directed DFS](chapter_4/directed_graphs/paths_dfs_directed.py)<br>
  - [Path detection directed BFS](chapter_4/directed_graphs/paths_bfs_directed.py)<br>
  - [Directed cycle detection](chapter_4/directed_graphs/directed_cycle.py)<br>
  - [Directed DFS Orderings](chapter_4/directed_graphs/directed_dfs_orderings.py)<br>
  - [Topological sort](chapter_4/directed_graphs/topological.py)<br>
  - [Strongly connected component detection (quadratic)](chapter_4/directed_graphs/scc_bruteforce.py)<br>
  - [Strongly connected component detection (Kosaraju)](chapter_4/directed_graphs/scc_kosaraju.py)<br>
  - [Transitive closure](chapter_4/directed_graphs/transitive_closure.py)<br>
  
- #### Undirected, edge-weighted Graphs <br>
  - [Edge](chapter_4/edge_weighted_graphs/edge.py)<br>
  - [Edge weighted graph](chapter_4/edge_weighted_graphs/edge_weighted_graph.py)<br>
  - [Minimum spanning tree (Lazy Prim)](chapter_4/edge_weighted_graphs/mst_lazyprim.py)<br>
  - [Minimum spanning tree (Eager Prim)](chapter_4/edge_weighted_graphs/mst_eagerprim.py)<br>
  - [Minimum spanning tree (Kruskal)](chapter_4/edge_weighted_graphs/mst_kruskal.py)<br>
  
- #### Edge-weighted Digraphs <br>
  - [Directed Edge](chapter_4/edge_weighted_digraphs/directed_edge.py)<br>
  - [Edge weighted digraph](chapter_4/edge_weighted_digraphs/edge_weighted_digraph.py)<br>
  - [Shortest path (Dijkstra)](chapter_4/edge_weighted_digraphs/sp_dijkstra.py)<br>
  - [Shortest path (edge-weighted DAG)](chapter_4/edge_weighted_digraphs/sp_acyclic.py)<br>
  - [Longest path (edge-weighted DAG)](chapter_4/edge_weighted_digraphs/lp_acyclic.py)<br>
  - [Parallel precedence-constrained scheduling (critical path method)](chapter_4/edge_weighted_digraphs/cpm.py)<br>
  - [Shortest path (Bellman-Ford)](chapter_4/edge_weighted_digraphs/sp_bellmanford.py)<br> 
  - [Arbitrage](chapter_4/edge_weighted_digraphs/arbitrage.py)<br>   
  

  ### Chapter 5
- #### Tries<br>
  - [256-Way Trie](chapter_5/trie/256way_trie.py)<br>
  - [R-Way Trie](chapter_5/trie/rway_trie.py)<br>
  - [Ternary search tries (TST)](chapter_5/trie/tst.py)<br>
- #### Substring Search<br>
  - [Brute force with backtracking substring search](chapter_5/substring_search/bruteforce_backtracking.py)<br>
  - [Knuth-Morris-Pratt substring search](chapter_5/substring_search/kmp.py)<br> 
