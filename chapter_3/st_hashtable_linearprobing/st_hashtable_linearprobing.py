# Title: st_hashtable_linearprobing.py
# Author: Ryan Borchardt

# I am implementing a symbol table with a hash table that uses linear probing.
# This symbol table does NOT support ordered operations because it is unordered (although it could support ordered operations, it just would take ~ linear time).

# Example:
# python st_hashtable_linearprobing.py

class ST_HashTable_LinearProbing:
    def __init__(self,M=4):
        self.M = M # size of hash table (initially)
        self.key_array = [None]*self.M
        self.value_array = [None]*self.M
        self.N = 0 # number of key/value pairs in the table
        
    def _hash_function(self,key):
        # Note that in the Python implementation we do NOT need to take the absolute value of the hash code
        # This is b/c of a difference in the modulo operator between Java and Python
            # In Java, the result has the sign of the dividend, so if hash(key) returns a negative number (which is very possible), then hash_code%M results in a negative number when we really want it to output a number between 0 and M-1.
            # In Python, the result has the sign of the divisor, and since M is a positive number, then hash_code%M is always a positive number between 0 and M-1, no matter what the sign of the hash_code is.
        return hash(key) % self.M
    
    
    # Ensures that our hash table is never more than half full
    # Keeps self.N / self.M between 1/8th and 1/2 full (M is always within a constant factor of N)
    # Each time _resize() is called, requires re-putting ALL key/value pairs with new hash table size
    # _resize() takes linear time. 
    # The put(), get() and delete() operations take constant amortized time.
    def _resize(self,factor):
        new_ST = ST_HashTable_LinearProbing(int(self.M*factor))

        for i in range(0,self.M):
            key_reput = self.key_array[i]
            value_reput = self.value_array[i]
            if key_reput is None: continue 
            new_ST.put(key_reput,value_reput)
        
        # Can essentially reassign self by reassigning all of its instance variables to the instance variables in new_ST
        self.M = new_ST.M
        self.key_array = new_ST.key_array
        self.value_array = new_ST.value_array
        self.N = new_ST.N
    
    def put(self,key,value):
        
        if self.N >= self.M//2: 
            self._resize(2)
            print(self.M)
        
        
        current_array_index = self._hash_function(key)
        while self.key_array[current_array_index] is not None:
            if self.key_array[current_array_index] == key: 
                self.value_array[current_array_index] = value
                return
            # Increments current_array_index by 1. 
            # If the current_array_index reaches the final entry in the hash table, the current_array_index is set back to zero:
            current_array_index = (current_array_index + 1) % self.M
        
        self.key_array[current_array_index] = key
        self.value_array[current_array_index] = value
        self.N+=1
        
        
    def get(self,key):
        current_array_index = self._hash_function(key)
        while self.key_array[current_array_index] != key:
            if self.key_array[current_array_index] is None:
                return None
            # Increments current_array_index by 1. 
            # If the current_array_index reaches the final entry in the hash table, the current_array_index is set back to zero:
            current_array_index = (current_array_index + 1) % self.M

        return self.value_array[current_array_index]
    
    def delete(self,key):
        current_array_index = self._hash_function(key)
        # First need to find the array_index for the key
        while self.key_array[current_array_index] != key:
            if self.key_array[current_array_index] is None: return None
            current_array_index = (current_array_index + 1) % self.M
        self.key_array[current_array_index] = None
        self.value_array[current_array_index] = None
        self.N -= 1
        # Need to re-put all key/value pairs in the cluster to the right of this index (from this index+1 to the first index w/ None value.
        # Some of the key/value pairs in this cluster may have had the same initial array_index as the deleted key and 
        # Need to re-put them so that a put() operation can find these keys
        current_array_index = (current_array_index +1) % self.M
        while self.key_array[current_array_index] is not None:
            key_reput = self.key_array[current_array_index]
            value_reput = self.value_array[current_array_index]
            self.key_array[current_array_index] = None
            self.value_array[current_array_index] = None
            self.N -= 1 # Need to decrement self.N only b/c the following put() operation increments self.N.
            self.put(key_reput,value_reput)
            current_array_index = (current_array_index +1) % self.M
        if self.N <= self.M//8: 
            print(self.N, self.M)
            self._resize(0.5)
            print(self.M)
    
    def contains(self,key):
        return self.get(key) is not None
        
    def size(self):
        return self.N
    
    def isEmpty(self):
        return self.N==0
        
    def __iter__(self):
        return ST_HashTable_LinearProbing._Iterator(self.key_array, self.M, self.N)
        
    class _Iterator:
        def __init__(self, keys, table_size, num_keys):
            self.keys = keys
            self.table_size = table_size
            self.num_keys = num_keys
            
            self.num_keys_processed = 0
            self.current_index = 0
        
        def __next__(self):
            if self.num_keys_processed == self.num_keys: raise StopIteration
            while self.keys[self.current_index] is None:
                self.current_index += 1
                if self.current_index == self.table_size: self.current_index=0
            returned_key = self.keys[self.current_index]
            self.num_keys_processed +=1
            self.current_index+=1
            if self.current_index == self.table_size: self.current_index=0
            return returned_key
                

def main():
    
    ST = ST_HashTable_LinearProbing()
    print(ST.isEmpty())
    
    ST.put('Tom', 24)
    print('Added Tom')
    ST.put('Bill', 55)
    print('Added Bill')
    ST.put('George', 78)
    print('Added George')
    ST.put('Timmy', 12)
    print('Added Timmy')
    ST.put('Bob', 43)
    print('Added Bob')
    ST.put('Terrance', 23)
    print('Added Terrance')
    ST.put('Howard', 31)
    print('Added Howard')
    ST.put('Buck', 94)
    print('Added Buck')
    ST.put('Sam', 19)
    print('Added Sam')
    ST.put('Jim', 61)
    print('Added Jim')
    
    for key in ST:
        print('Key:',key)
    
    print("Howard's age: ",ST.get('Howard'))
    print(ST.N, ST.M)    
    ST.delete('Howard')
    print('Deleted Howard',ST.N, ST.M)   
    ST.delete('Tom')
    print('Deleted Tom',ST.N, ST.M)   
    ST.delete('Buck')
    print('Deleted Buck',ST.N, ST.M)   
    ST.delete('Jim')
    print('Deleted Jim',ST.N, ST.M)   
    ST.delete('George')
    print('Deleted George',ST.N, ST.M)   
    ST.delete('Sam')
    print('Deleted Sam',ST.N, ST.M)   
    ST.delete('Timmy')
    print('Deleted Timmy',ST.N, ST.M)   
    ST.delete('Bill')
    print('Deleted Bill',ST.N, ST.M)   
    
    print('Iterating after deleting several keys:')
    for key in ST:
        print('Key:',key)
    
        
    print(ST.isEmpty())
    print(ST.size())
    print(ST.contains('Timmy'))
    print(ST.contains('Gary'))
    
    print(ST.get('Bob'))
    print(ST.get('Ricky'))
    
if __name__=="__main__": main()