# Title: merge_sort.py
# Author: Ryan Borchardt

# This module implements the sort (top down merge sort) function along with other supporting functions. 

# The test client takes in a file of strings from standard input and sorts in alphabetical order.

# The sort (merge sort) function has an order of growth of linearithmic time (N*lg(N)). 
    # Best case (input is already sorted): 
    # Worst case (input is sorted in reverse order): 
    # Random case (input is in a random order): 

# Example:
# python merge_sort.py < tiny16.txt


import sys

def _merge(a,lo,mid,hi,sorted_array_segment):
    n = hi - lo
    least_first_half = lo
    least_second_half = mid
    
    for k in range(n):
        # If least_first_half == mid, then all of the elements from the first_half have been added to sorted_array_segment. All that is left are the remaining elements in the 2nd half.
        if least_first_half == mid:
            sorted_array_segment[k] = a[least_second_half]
            least_second_half += 1
        # If least_second_half == hi, then all of the elements from the second_half have been added to sorted_array_segment. All that is left are the remaining elements in the 1st half.
        elif least_second_half == hi:
            sorted_array_segment[k] = a[least_first_half]
            least_first_half += 1
        elif a[least_first_half] <= a[least_second_half]:
            sorted_array_segment[k] = a[least_first_half]
            least_first_half += 1
        elif a[least_second_half] < a[least_first_half]:
            sorted_array_segment[k] = a[least_second_half]
            least_second_half +=1
    
    a[lo:hi] = sorted_array_segment[0:n]
            


def _recursive_sort(a,lo,hi,sorted_array_segment):
    mid = (hi+lo)//2 ## Floored division, so if odd # of elements, first half [lo:hi) has floor(N/2) elements and second half has ceil(N/2) elements
    n = hi - lo
    if n == 1: return
    _recursive_sort(a,lo,mid,sorted_array_segment)
    _recursive_sort(a,mid,hi,sorted_array_segment)
    _merge(a,lo,mid,hi,sorted_array_segment)



def sort(a):
    n = len(a)
    lo = 0
    hi = n
    sorted_array_segment = list()
    for i in range(n):
        sorted_array_segment.append(0) 
    _recursive_sort(a,lo,hi,sorted_array_segment)
    
        
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