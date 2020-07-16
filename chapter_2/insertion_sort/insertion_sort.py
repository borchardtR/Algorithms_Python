# Title: insertion_sort.py
# Author: Ryan Borchardt

# This module implements the sort (insertion sort) function along with other supporting functions. 

# The sort (insertion sort) function has an order of growth of quadratic time. 
    # Best case (input is already sorted): N-1 compares (each compare consists of 2 array accesses and one compare) and 0 exchanges (linear).
    # Worst case (input is sorted in reverse order): N^2/2 compares and N^2/2 exchanges (quadratic)
    # Random case (input is in a random order): N^2/4 compares and N^2/4 exchanges (half the time (on average) a given element a[j] is less than a[j-1]) (quadratic)

# Comparing insertion sort to selection sort:
    # Best case (input is already sorted): 
        # Insertion sort: N-1 compares vs Selection Sort: ~N^2/2 compares (Insertion sort performs much better than selection sort)
    # Worst case (input is sorted in reverse order): N^2/2 compares and N^2/2 exchanges
        # Insertion sort: ~N^2/2 compares and ~N^2/2 exchanges vs Selection Sort: ~N^2/2 compares and N exchanges (Insertion sort performs worse than selection sort)
    # Random case (input is in a random order): N^2/4 compares and N^2/4 exchanges (half the time (on average) a given element a[j] is less than a[j-1])
        # Insertion sort: ~N^2/4 compares and ~N^2/4 exchanges vs Selection sort: ~N^2/2 compares and N exchanges (Insertion sort performs about the same as selection sort)

# The test client takes in a file of strings from standard input and sorts in alphabetical order.

# Example:
# python insertion_sort.py < tiny.txt

import sys


def sort(a):
    for i in range(1,len(a)):
        for j in range (i,0,-1): 
            if a[j]>=a[j-1]: break
            else: exch(a,j,j-1)
        
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
    sort(a)
    print(a)
    assert isSorted(a)
    #show(a)


if __name__=="__main__": main()