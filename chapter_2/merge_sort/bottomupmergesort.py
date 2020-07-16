# Title: bottomupmergesort.py
# Date: 6/6/2020
# Author: Ryan Borchardt

# Works for input for length N = 2^n, doesn't work for input that isn't a power of 2 yet. Needs further study. Need to revisit. Skipped for now b/c it was taking too much time.

# This module implements the sort (top down merge sort) function along with other supporting functions. 

# The test client takes in a file of strings from standard input and sorts in alphabetical order.

# % more tiny.txt
# S O R T E X A M P L E


# The sort (merge sort) function has an order of growth of linearithmic time (N*lg(N)). 
    # Best case (input is already sorted): 
    # Worst case (input is sorted in reverse order): 
    # Random case (input is in a random order): 



import sys
import math

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
            


def _sort(a,lo,hi,sorted_array_segment):
    mid = (hi+lo)//2
    N = hi
    n = int(math.log(N,2))
    print(n)
    
    # of layers in tree
    # from k=0 to n-1, the kth level from top depicts:
    #   2^k subarrays
    #   each of length 2^(n-k)
    
    #N=2^n
    # from k=0 to n-1, the kth level from the bottom depicts:
    #   2^(n-k) subarrays (if N=16, n=4 and at k=0, there are 2^4-0 = 16 subarrays are combined to form 8. If N=16, n=4 and at k=1, there are 2^4-1 = 8 subarrays are combined to form 4. At k = n-1 = 3, we are combing 2 subarrays (final)
    #   each of length 2^k
    
    # This loop is from each layer in the tree, starting at the bottom and working its way to include the 2nd from the top (when we are combining the final 2 halves).
    for k in range(0,n):
        num_sub_arrays = int(2**(n-k))
        length_sub_array = int(2**k)
        print(length_sub_array)
        num_sub_array_pairs = int(num_sub_arrays/2)
        print("k,num_sub_arrays,length_sub_array,num_sub_array_pairs", k,num_sub_arrays,length_sub_array,num_sub_array_pairs)
        # This loop is for merging each pair of subarrays
        for i in range(0,num_sub_array_pairs):
            lo = int(length_sub_array*2*i)
            mid = int(lo + length_sub_array)
            hi = int((mid-lo) + mid)
            print("lo,mid,hi", lo,mid,hi)
            _merge(a,lo,mid,hi,sorted_array_segment)



def sort(a):
    N = len(a)
    lo = 0
    hi = N
    sorted_array_segment = list()
    for i in range(N):
        sorted_array_segment.append(0) 
    _sort(a,lo,hi,sorted_array_segment)
    
        
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