# Title: quicksort.py
# Author: Ryan Borchardt


# This module implements the sort (quick sort) function along with other supporting functions.  

# The test client takes in a file of strings from standard input and sorts in alphabetical order.

# % more quicksort_text.txt
# Q U I C K S O R T E X A M P L E

# random.seed(1)
# random.shuffle(['Q', 'U', 'I', 'C', 'K', 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']) 
# results in:
# ['I', 'X', 'Q', 'L', 'O', 'S', 'C', 'T', 'R', 'A', 'E', 'U', 'M', 'P', 'E', 'K']

# Time complexity is ~ N*lg(N) in both the best and average-case.
# Space complexity is ~lg(N) in both the best and average-case (the call stack has a max of ~lg(N) frames on it at a time, each with constant space).

# Time complexity is ~N^2 in the worst-case (this is incredibly rare as we randomly shuffle the array beforehand so getting an array that is in reverse-order is very, very unlikely).
# Space complexity is ~N in the worst-case (the call stack has a max of ~N frames on it at a time, each with constant space)

# Note that Python has a built-in sorted() function and a List.sort() method.
    # Both utilize the timsort algorithm, which is a hybrid of the mergesort and insertion sort algorithms.

    
# Example:
# python quicksort.py < quicksort_text.txt



import sys
import random

def _partition(a,lo,hi):
    #Initialize pointer i
    i = lo
    #Initialize pointer j
    j = hi+1
    
    # Determine the paritioning element, v, (in this case we always choose a[lo] (this is an arbitrary choice b/c we have already shuffled the array)
    v = a[lo]
    print('Bounds of subarray being partitioned from lo to hi:', lo, 'to ', hi)
    print('Partitioning element:', v)
    
    while True:
        i = i+1
        j = j-1
        
        # Increment i until a[i] is not less than the partitioning element and while i <= hi (so that the pointer doesn't go outside of bounds of the subarray)
        while (a[i] < v) and (i <= hi):
            i = i+1
        # Decrement j until a[j] is not greater than the partitioning element and while j >= lo (so that the pointer doesn't go outside of bounds of the subarray). Note that the and j>= lo is redundant b/c if j=lo, then a[j] is not > v so it won't continue anyway.
        while (a[j] > v) and (j >= lo):
            j = j-1
        
        # If i and j cross, then we know we have found the final index position of the partitioning element. Swap the partitioning element with a[j] so that all of the elements to the left of the final index position of the partitioning element are less than the partitioning element and so that all of the elements to the right of the final index position of the partitioning element are greater than the partioning element.
        if j <= i: break
        
        # if i and j have not crossed yet:   
        if i < j:
        # a[i] and a[j] are on the wrong sides of the final index of the partitioning element. swap a[i] and a[j] so that they will be on the correct side of the final position of the partitioning element   
            exch(a,i,j)
            print('Exchanged: a[',i,'] with a[',j,'].')
    
    # The while loop above has been broken b/c i and j have crossed (see if statement). Swap the partitioning element with a[j] so that all of the elements to the left of the final index position of the partitioning element are less than the partitioning element and so that all of the elements to the right of the final index position of the partitioning element are greater than the partioning element.     
    print('Exchanged the partitioning element', v, 'at index:',lo, 'with a[j]', a[j], 'at index:',j)
    exch(a,lo,j)
    
    print('Final index position:', j, 'for the partitioning element:', v)
    print(a)
    print('Returned j value:', j)
    print('\n')
    # Return the final index position of the partitioning element
    return j
            


def _sort(a,lo,hi):
    if hi <= lo: 
        print('_sort returned without partitioning b/c hi <= lo:',hi,'<=',lo,'\n')
        return
    j = _partition(a,lo,hi)
    _sort(a,lo,j-1)
    _sort(a,j+1,hi)




def sort(a):
    N = len(a)
    lo = 0
    hi = N-1
    random.seed(1)
    random.shuffle(a)
    print('Shuffled array with seed(1):',a)
    print('\n')
    _sort(a,lo,hi)
    
        
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
    show(a)


if __name__=="__main__": main()