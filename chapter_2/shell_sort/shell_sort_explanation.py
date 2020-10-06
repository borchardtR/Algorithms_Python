# Title: shell_sort_explanation.py
# Author: Ryan Borchardt

# This module implements the sort (shell sort) function along with other supporting functions. 

# I implemented this in a unique way that makes intuitive sense to me. There is a substantial amount of code that is to simply help explain what is happening at each step.

# Requires a command line argument to set the length of the unsorted array.

# Example:
# python shell_sort_explanation.py 100


import sys
import random

def sort(a):
    N = len(a)
    h = 1
    # Determines the starting increment for each h-sort:
    while h < int(N/3): h = 3*h + 1
    
    # Each loop corresponds to each h-sort.
    while h >= 1: 
        print('\n')
        print(h,'-sort:')
        print('Perform insertion sort on the following indexes:')
        overall_array = []
        # Each loop determines each of the subarrays:
        # The number of subarrays for each h-sort varies between 1 and h subarrays.
        for i in range(0,h,1):
            subarray = []
            j = h
            subarray.append(i)
            while i + j < N:
                subarray.append(i+j)
                j = j+h
            if len(subarray) > 1: 
                overall_array.append(subarray)
                # Perform insertion sort on the subarray:
                for i in range(1,len(subarray)):
                    for j in range (i,0,-1): 
                        if a[subarray[j]]>=a[subarray[j-1]]: break
                        else: exch(a,subarray[j],subarray[j-1])
        print(overall_array)
        h = h//3
        
            
         
                
            
    
    
        
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
    random.seed(1)
    N= int(sys.argv[1])
    a = []
    for i in range(N):
        a.append(random.uniform(0,100))
    print('unsorted array:')
    print(a)
    sort(a)
    assert isSorted(a)
    print('sorted array:')
    print(a)
    #show(a)
    #print(array_strings)


if __name__=="__main__": main()