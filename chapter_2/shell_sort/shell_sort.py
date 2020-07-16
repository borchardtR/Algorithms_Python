# Title: shell_sort.py
# Date: 6/2/2020
# Author: Ryan Borchardt

# This module implements the sort (shell sort) function along with other supporting functions. 

# The test client takes in a file of strings from standard input and sorts in alphabetical order.

# Example:
# python shell_sort.py < tiny.txt

import sys


def sort(a):
    N = len(a)
    h = 1
    # Determines the starting increment for each h-sort:
    while h < int(N/3): h = 3*h + 1
    
    # Each loop corresponds to each h-sort.
    while h >= 1: 
        # Each of this for loop compares 
        for i in range(h,N,1):
            j=i
            while j >= h:
                if a[j] > a[j-h]: break
                exch(a,j,j-h)
                j = j - h
        h = int(h/3)
                
            
    
    
        
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
    #assert isSorted(a)
    #show(a)
    #print(array_strings)


if __name__=="__main__": main()