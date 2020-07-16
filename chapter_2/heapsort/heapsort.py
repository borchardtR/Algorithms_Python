# Title: heapsort.py
# Author: Ryan Borchardt


# This module implements the sort (heapsort) function along with other supporting functions.  

# Example:
# python heapsort.py < quicksort_text.txt


import sys


def sort(a):
    # Heap construction
    # Need to convert the array into a heap that is heap-ordered.
    # Note that I am using a 0-indexed heap for the _sink() operation (the sink() function I implemented for priority queues is 1-indexed).
    number_nodes = len(a)
    
    # Start at the largest-indexed node that has a child:
    largest_indexed_node_with_child = (number_nodes-1)//2
    
    # sink the node starting at largest_indexed_node_with_child and working way up to the root node (0):
    for i in range(largest_indexed_node_with_child,-1,-1):
        _sink(a,i,number_nodes)
        #print(i)
        #print(a)
    # The end result: the array a has been rearranged into a heap.
    print('Heap:\n', a)
    
    # Next need to perform the sortdown whereby:
    while number_nodes > 1:
        # Exchange the root node (current maximum) with the largest_indexed_node
        largest_index_node = number_nodes-1
        exch(a,0,largest_index_node)
        # Reduce the number_nodes by 1, effectively removing the maximum from the heap
        number_nodes -= 1
        # Perform the sink operation on the new node to restore the heap order.
        _sink(a,0,number_nodes)
        # Repeat this process for each node
    
def _sink(a,i,number_nodes):
    parent_node = i
    child_node = 2*i+1 
    
    while child_node < number_nodes:
        # Need to select greatest child node:
        # First need to confirm that the node has two children:
        if child_node+1 < number_nodes:
            if a[child_node] < a[child_node-1]: child_node = child_node-1
        # If parent node is >= child node, then the sink operation is complete
        if a[parent_node] >= a[child_node]: break
        
        exch(a,parent_node,child_node)
        
        parent_node = child_node
        child_node = 2*parent_node+1
    
    
    
        
def less(v, w):
    return v < w 
    
def exch(a, i, j):
    temp_val = a[i]
    a[i] = a[j]
    a[j] = temp_val
    
def show(a):
    for element in a:
        print(element + "   ")
    print("\n")
    
def isSorted(a):
    for i in range(1,len(a)):
        if less(a[i],a[i-1]): return False
    return True
    
def main():
    # Array of strings
    a = sys.stdin.readline().split(" ")
    print('Unsorted array:\n ',a)
    sort(a)
    assert isSorted(a)
    print('Sorted array:\n',a)


if __name__=="__main__": main()