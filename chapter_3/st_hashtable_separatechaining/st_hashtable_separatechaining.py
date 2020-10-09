# Title: st_hashtable_separatechaining.py
# Author: Ryan Borchardt

# I am implementing a symbol table with a hash table that uses separate chaining.
# This symbol table does NOT support ordered operations because it is unordered (although it could support ordered operations, it just would take ~ linear time).

# Note that I am explicitly defining linked lists by defining the Node class

# Example:
# python st_hashtable_separatechaining.py

class ST_HashTable_SeparateChaining:
    def __init__(self,M=4):
        self.M = M # size of hash table
        self.array = [None]*self.M # array of length M (initially empty)
        self.N = 0 # total number of key/value pairs in the symbol table
        
    class Node:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.next = None
        
    def _hash_function(self,key):
        # Note that in the Python implementation we do NOT need to take the absolute value of the hash code
        # This is b/c of a difference in the modulo operator between Java and Python
            # In Java, the result has the sign of the dividend, so if hash(key) returns a negative number (which is very possible), then hash_code%M results in a negative number when we really want it to output a number between 0 and M-1.
            # In Python, the result has the sign of the divisor, and since M is a positive number, then hash_code%M is always a positive number between 0 and M-1, no matter what the sign of the hash_code is.
        return hash(key) % self.M
        
    # Ensures that the average linked list length is always between 0.125 and 0.50
    # Keeps self.N / self.M between 1/8th and 1/2 (M is always within a constant factor of N)
    # Each time _resize() is called, requires re-putting ALL key/value pairs with new hash table size
    # _resize() takes linear time. 
    # The put(), get() and delete() operations take constant amortized time.
    def _resize(self,factor):
        new_ST = ST_HashTable_SeparateChaining(int(self.M*factor))
        
        # Need to re-put ALL key/value pairs....
        for node in self:
            new_ST.put(node.key,node.value)
            
        self.M = new_ST.M
        self.array = new_ST.array 
            
    
    def put(self,key,value):
        if self.N/self.M >= 0.5: self._resize(2)
        
        key_array_index = self._hash_function(key)
        new_node = ST_HashTable_SeparateChaining.Node(key,value)
        old_node = self.array[key_array_index]
        new_node.next = old_node
        self.array[key_array_index] = new_node
        self.N +=1
    
    def _get(self,key,current_node):
        if current_node == None: return None
        if current_node.key == key: return current_node.value
        return self._get(key,current_node.next)
        
        
    def get(self,key):
        key_array_index = self._hash_function(key)
        current_node = self.array[key_array_index]
        return self._get(key,current_node)
        
    
    def delete(self,key):
        key_array_index = self._hash_function(key)
        current_node = self.array[key_array_index]
        if current_node == None: 
            print(key, ' is not in the symbol table')
            return
        # If the first node has the key, need to reassign the reference at the key_array_index position to the node after this one:
        if current_node.key == key:
            self.array[key_array_index] = current_node.next
            self.N -= 1
            if (self.N>0) and (self.N/self.M) <= 1/8: self._resize(0.5)
            return
        while current_node != None:
            # If node after current node has the key, reassign current_node.next to the node after the node with the key (current_node.next.next)
            if current_node.next.key == key: 
                current_node.next = current_node.next.next
                self.N -= 1
                if (self.N>0) and (self.N/self.M) <= 1/8: self._resize(0.5)
            current_node = current_node.next
            return
        if current_node == None: 
            print(key, ' is not in the symbol table')
            return        
        
    def contains(self,key):
        return self.get(key)!=None
        
    def size(self):
        return self.N 
        
    def isEmpty(self):
        return self.N==0
    
    
    def __iter__(self):
        return ST_HashTable_SeparateChaining._Iterator(self.M,self.array,self.N)
        
    class _Iterator:
        def __init__(self,M,array,N):
            self.array = array
            self.node_limit = N 
            self.nodes_processed = 0
            self.current_array_index = 0
            self.current_node = self.array[self.current_array_index]
        
        def __next__(self):
            if self.nodes_processed==self.node_limit: raise StopIteration
            # Skip to next array index that has a linked list:
            while self.current_node == None: 
                self.current_array_index += 1
                self.current_node = self.array[self.current_array_index]
            returned_node = self.current_node
            self.nodes_processed += 1
            self.current_node = self.current_node.next
            return returned_node   
    
    def __getitem__(self, key):
        return self.get(key)
        
    def __setitem__(self, key, value):
        return self.put(key, value)

def main():
    
    ST = ST_HashTable_SeparateChaining()
    print(ST.isEmpty())
    print(ST.N, ST.M)
    ST.put('Tom', 24)
    print('Added Tom',ST.N, ST.M)
    ST.put('Bill', 55)
    print('Added Bill',ST.N, ST.M)
    ST.put('George', 78)
    print('Added George',ST.N, ST.M)
    ST.put('Timmy', 12)
    print('Added Timmy',ST.N, ST.M)
    ST.put('Bob', 43)
    print('Added Bob',ST.N, ST.M)
    ST.put('Terrance', 23)
    print('Added Terrance',ST.N, ST.M)
    ST.put('Howard', 31)
    print('Added Howard',ST.N, ST.M)
    ST.put('Buck', 94)
    print('Added Buck',ST.N, ST.M)
    ST.put('Sam', 19)
    print('Added Sam',ST.N, ST.M)
    ST.put('Jim', 61)
    print('Added Jim',ST.N, ST.M)
    
    for node in ST:
        print('Key:',node.key)
    
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
    for node in ST:
        print('Key:',node.key)
    
        
    print(ST.isEmpty())
    print(ST.size())
    print(ST.contains('Timmy'))
    print(ST.contains('Gary'))
    
    print(ST.get('Bob'))
    print(ST.get('Ricky'))
    
if __name__=="__main__": main()