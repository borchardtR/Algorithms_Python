# Title: mergesort_iterative.py
# Author: Ryan Borchardt

# Bottom-up merge sort is the iterative version of merge sort.
# Top-down merge sort is the recursive version of merge sort.

# The merge() function is the exact same in both the bottom-up and top-down versions.

# The only difference is the order in which the subarrays are sorted.

# python mergesort_iterative.py < len_6.txt      
    
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


def sort(a):
    a_length = len(a)
    aux = a[:]
    subarray_size = 1
    
    while subarray_size < a_length:
        print("subarray size: ", subarray_size)
        for i in range(0, a_length, subarray_size*2): 
            print(i, i+subarray_size, min(i+subarray_size*2, a_length))
            merge(a, i, i+subarray_size, min(i+subarray_size*2, a_length), aux)
        
        print("\n\n")
        subarray_size *= 2



def main():
    # Array of strings
    a = sys.stdin.readline().split(" ")
    print(a)
    sort(a)
    print(a)


if __name__=="__main__": main()