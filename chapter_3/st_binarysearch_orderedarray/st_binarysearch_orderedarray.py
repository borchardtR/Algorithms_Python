# Title: st_binarysearch_orderedarray.py
# Date: 6/23/2020
# Author: Ryan Borchardt

# I created a symbol table by implementing an ordered array (I am using the Python list data structure which is a dynamic array). It utilizes binary search.
# I will be using the Python list as if it is a fixed-size array (ie I will be implementing my own resizing method).

# This is an implementation for the ordered symbol table API on page 366 of Sedgewick/Wayne's Algorithms.
# Both the put() and get() methods use binary search.
# put() uses binary search b/c first it searches the symbol table to see if the key is already in the symbol table before creating a new key:value entry. 
# However, put() overall takes linear time b/c each insertion into the key and value arrays() involves shifting the elements at and to the right of the index over 1.
# This symbol table DOES support ordered operations.


# Cost to build full table: (N^2)/2 
# Cost for search hit: N/2 (average), N (worst-case)
# Cost to add new key: N (for both average and worst)
# Cost to update existing key: N/2 (average), N (worst-case)

# Example:
# python st_binarysearch_orderedarray.py

class ST_binarysearch_orderedarray:
    def __init__(self):
        self.key_array = [None]*1
        self.value_array = [None]*1
        # number of entries in each array
        self.n = 0
        
    class _Iterator:
        def __init__(self, key_array):
            self.key_array = key_array
            self.current_index=0
        
        def __next__(self):
            returned_key = self.key_array[self.current_index]
            self.current_index+=1
            if returned_key == None: raise StopIteration
            return returned_key
        
    def __iter__(self):
        return ST_binarysearch_orderedarray._Iterator(self.key_array)
    
    
    def _resize(self,factor):
        intermediate_key_array = self.key_array
        intermediate_value_array = self.value_array
        
        current_array_size = len(self.key_array)
        self.key_array = [None]*factor*current_array_size
        self.value_array = [None]*factor*current_array_size
        
        for i in range(current_array_size):
            self.key_array[i] = intermediate_key_array[i]
            self.value_array[i] = intermediate_value_array[i]
            
    
    # rank() uses binary search to find the correct index location of the key
    def rank(self,key):
        lo = 0
        hi = self.n-1
        # Note that if the arrays are empty, hi=-1 and the while loop doesn't execute and lo=0 is returned.
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if key == self.key_array[mid]: return mid
            if key > self.key_array[mid]: lo = mid+1
            if key < self.key_array[mid]: hi = mid-1
        return lo
        
        
    def put(self,key,value):
        # First check to see if key already in symbol table:
        
        key_index = self.rank(key)
        # If key already in symbol table, update the value.
        if (self.n) > 0 and key == self.key_array[key_index]: self.value_array[key_index] = value
        
        # If key not already in symbol table, move all keys/values at and after index over 1 index and insert new key/value pair:
        else:
            # First need to check and see if array needs to be expanded in size:
            if self.n >= len(self.key_array):
                self._resize(2)
            
            for i in range(self.n,key_index,-1):
                self.key_array[i] = self.key_array[i-1]
                self.value_array[i] = self.value_array[i-1]
            self.key_array[key_index] = key
            self.value_array[key_index] = value
            self.n += 1
            
    def get(self,key):
        key_index = self.rank(key)
        if key == self.key_array[key_index]: return self.value_array[key_index]
        else: return None
        
    def contains(self,key):
        return self.get(key) != None
        
    def size(self):
        return self.n
        
    def isEmpty(self):
        return self.n == 0
    
    def min(self):
        return self.key_array[0]
    
    def max(self):
        return self.key_array[self.n-1]
        
    def floor(self,key):
        key_index = self.rank(key)
        if self.key_array[key_index] == key: return key
        else: return self.key_array[key_index-1]
        
    def ceiling(self,key):
        key_index = self.rank(key)
        return self.key_array[key_index]
        
    def select(self,rank):
        return self.key_array[rank]
        
    def deleteMin(self):
        for i in range(0,self.n-1):
            self.key_array[i] = self.key_array[i+1]
            self.value_array[i] = self.value_array[i+1]
        self.key_array[self.n-1] = None
        self.value_array[self.n-1] = None
        self.n -= 1
        # Check to see if arrays needs to be shrunk in size:
        if self.n < int(0.25*len(self.key_array)): self._resize(0.5)
        
    def deleteMax(self):
        self.key_array[self.n-1] = None
        self.value_array[self.n-1] = None
        self.n -= 1
        # Check to see if arrays needs to be shrunk in size:
        if self.n < int(0.25*len(self.key_array)): self._resize(0.5)
        
    def delete(self,key):
        key_index = self.rank(key)
        if self.key_array[key_index] != key: raise Exception('Key is not in symbol table.')
        else:
            for i in range(key_index,self.n-1):
                self.key_array[i] = self.key_array[i+1]
                self.value_array[i] = self.value_array[i+1]
            self.key_array[self.n-1] = None
            self.value_array[self.n-1] = None
            self.n -= 1
            # Check to see if arrays needs to be shrunk in size:
            if self.n < int(0.25*len(self.key_array)): self._resize(0.5)
            
         
        
            
def main():
    ST = ST_binarysearch_orderedarray()
    ST.put('Tom', 24)
    ST.put('Bill', 55)
    ST.put('George', 78)
    ST.put('Timmy', 12)
    ST.put('Bob', 43)
    ST.put('Terrance', 23)
    ST.put('Howard', 31)
    ST.put('Buck', 94)
    ST.put('Sam', 19)
    ST.put('Jim', 61)
    
    
    print(ST.get('Bob'))
    
    for i in ST:
        print(i)
        
    print(ST.isEmpty())
    print(ST.size())
    print(ST.min())
    print(ST.max())
    print(ST.contains('Sam'))
    print(ST.contains('Johnny'))
    
    print(ST.floor('George'))
    print(ST.floor('Craig'))
    
    print(ST.ceiling('George'))
    print(ST.ceiling('Craig'))
    
    print(ST.select(2))
    
    print('\n')
    print(ST.size())
    ST.deleteMin()
    ST.deleteMin()
    ST.deleteMin()
    print(ST.size())
    for i in ST:
        print(i)
    
    
    print('\n')
    print(ST.size())
    ST.deleteMax()
    ST.deleteMax()
    print(ST.size())
    for i in ST:
        print(i)
        
    ST.put('Red', 88)
    ST.put('Frankie',14)
    ST.put('Darrol',29)
    ST.put('Pete',42)
    ST.put('Richard',38)
    ST.put('Shane',67)
    print('\n')
    print(ST.size())
    for i in ST:
        print(i)
    
    ST.delete('Red')
    print('\n')
    print(ST.size())
    for i in ST:
        print(i)
        
    #ST.delete('Donaldson')
    
    
    
if __name__=="__main__": main()