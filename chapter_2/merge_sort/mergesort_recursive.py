# Title: mergesort_recursive.py
# Author: Ryan Borchardt

# Bottom-up merge sort is the iterative version of merge sort.
# Top-down merge sort is the recursive version of merge sort.

# The merge() function is the exact same in both the bottom-up and top-down versions.

# The only difference is the order in which the subarrays are sorted.

# Time complexity is ~ N*lg(N) in all cases.
# Space complexity is ~N in all cases. 
    # the auxillary array has a length of N. 
    # Also takes an additional lg(N) space (max # of frames on the call stack is lg(N), each of constant space)
    # ~N + lg(N) = ~N

# python mergesort_recursive.py < len_6.txt      
    
import sys

def merge(a, lo, mid, hi, aux):
    i = lo
    j = mid
    n = hi -lo
    for k in range(n):
        if i == mid:
            aux[k] = a[j]
            j += 1
        elif j == hi:
            aux[k] = a[i]
            i += 1
        elif a[i] <= a[j]:
            aux[k] = a[i]
            i += 1
        elif a[j] < a[i]:
            aux[k] = a[j]
            j+=1
    a[lo:hi] = aux[0:n]

# Reminder that in Python (and most programming languages), it is pass by reference, so each entry on the call stack stores references to the arguments, not the values themselves
# This means that passing an array of length n into a recursive function does NOT take O(n) space for each frame on the call stack -> it takes O(1) space for each frame b/c only the references are stored in the memory,
# Also keep in mind that arrays are mutable but integers, floats etc are immutable so even though Python is pass by reference, changing local int variables will not effect the calling function's local int variables
# However,if you were to CREATE an array in a recursive function that is called multiple times in the call stack, each frame would take O(n) space!

def _sort(a, lo, hi, aux):
    if hi-lo == 1:
        return
    mid = lo + (hi-lo)//2
    
    _sort(a,lo,mid,aux)
    _sort(a,mid,hi,aux)
    merge(a,lo,mid,hi,aux)
    


def sort(a):
    lo = 0
    hi = len(a)
    aux = a[:]
    
    _sort(a,lo,hi,aux)



def main():
    # Array of strings
    a = sys.stdin.readline().split(" ")
    print(a)
    sort(a)
    print(a)


if __name__=="__main__": main()