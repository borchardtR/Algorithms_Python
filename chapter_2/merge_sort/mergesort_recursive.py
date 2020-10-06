# Title: mergesort_recursive.py
# Author: Ryan Borchardt

# Bottom-up merge sort is the iterative version of merge sort.
# Top-down merge sort is the recursive version of merge sort.

# The merge() function is the exact same in both the bottom-up and top-down versions.

# The only difference is the order in which the subarrays are sorted.

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