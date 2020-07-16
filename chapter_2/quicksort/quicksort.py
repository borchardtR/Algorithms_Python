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

# The sort (quick sort) function has an order of growth of 
    # Best case (input is already sorted): 
    # Worst case (input is sorted in reverse order): 
    # Random case (input is in a random order): 
    
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
        
        
    #Decrement j until a[j] is not greater than the partitioning element
    
    # Need to swap a[i] and a[j] b/c they are each on the wrong side of the final index position of the partitioning element. Note that we are closing in on the final index position of the partitioning element as i and j get closer. (once i and j have crossed, we know the final index position of the partitioning element is j)
    # This operation supports the goal of rearranging a such that all of the elements to the left of the final index position of the partitioning element are less than the partitioning element and all of the elements to the right of the 
    exch(a,i,j)
    
    # When the pointers have crossed, this is a signal that we have found the final index position of the partitioning element such that all of the elements to the left of it are less than the partitioning element and all of the elements to the right of it are greater than the partitioning element
    # Need to swape the partitioning element with a[j] b/c note how it results in all the elements to the left of the partitioning element being less than the partitioning element and all of the elements to the right of the partitioning element being greater than the partitioning element.
    exch(a,lo,j)
    
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