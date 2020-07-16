# Title: selection_sort.py
# Author: Ryan Borchardt

# This module implements the sort (selection sort) function along with other supporting functions. 


# Note that I don't need to worry about having a Comparable interface. This is because Python supports operator overloading with built-in special methods. 
# Also I am pretty sure Python doesn't use sub-typing interface inheritence (Pyhton definitely does use sub class inheritence, however (p.479 onsidered comparable and sort() will work (p.479 of Sedgewick/Wayne's Intro to Programming in Python).

# Any object that implements these 6 specific special methods (__lt__,__le__,__ge__,__gt__, __eq___, __ne__) that overload the comparison operators and establishes a total order (antisymmetry, transitivity and tolatality) is considered comparable and sort() will work (p.472-479 of Sedgewick/Wayne's Intro to Programming in Python).

# The isSorted() function takes linear time
# The show() function takes linear time
# The exch() function takes constant time
# The less() function takes constant time

# The sort (selection sort) function has an order of growth of quadratic time and is insensitive to the input. 
    # Best case (input is already sorted): ~N^2/2 compares and N exchanges
    # Worst case (input is sorted in reverse order): ~N^2/2 compares and N exchanges
    # Random case (input is in a random order): ~N^2/2 compares and N exchanges

# The test client takes in a file of strings from standard input and sorts in alphabetical order.

# Example:
# python selection_sort.py < tiny.txt


import sys


def sort(a):
    for i in range(len(a)):
        a_min = a[i]
        a_min_index = i
        for j in range(i+1,len(a)):
            if a[j] < a_min: 
                a_min = a[j]
                a_min_index = j
        exch(a,i,a_min_index)

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
