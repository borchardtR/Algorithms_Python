# Title: st_sequentialsearch_unorderedlinkedlist.py
# Author: Ryan Borchardt

# I created a symbol table by implementing an unordered linked list. It utilizes sequential search.
# This is an implementation for the basic symbol table API on page 363 of Sedgewick/Wayne's Algorithms.
# Both the put() and get() methods use sequential search.
# put() uses sequential search b/c first it must check through the symbol table (sequentially) to see if the key is already in the symbol table before creating a new key:value entry.

# This symbol table does NOT support ordered operations because it is unordered (although it could support ordered operations, it just wouldn't be as efficient).


# Cost to build full table: (N^2)/2 
# Cost for search hit: N/2 (average), N (worst-case)
# Cost to add new key: N (for both average and worst)
# Cost to update existing key: N/2 (average), N (worst-case)

# Example:
# python st_sequentialsearch_unorderedlinkedlist.py


class ST_unordered_linkedlist:
    def __init__(self):
        self.linked_list = None
        self.node_count = 0
        
    class Node:
        def __init__(self,key, value, next):
            self.key = key
            self.value = value
            self.next = next
            
    class linkedlist_Iterator:
        def __init__(self, linked_list):
            self.first_node = linked_list
            self.current_node = 1
            
        def __next__(self):
            if self.first_node == None: raise StopIteration
            returned_node = self.first_node
            self.first_node = self.first_node.next
            return returned_node
        
        
        
    def put(self, key, value):
        # Need to iterate through symbol table to see if key is already in symbol table:
        if self.node_count == 0:
            new_node = ST_unordered_linkedlist.Node(key, value, self.linked_list)
            self.linked_list = new_node
            self.node_count += 1
            return
            
        for node in self:
            if node.key == key: 
                node.value = value 
                return
        new_node = ST_unordered_linkedlist.Node(key, value, self.linked_list)
        self.linked_list = new_node
        self.node_count += 1
        
    def get(self, key):
        for node in self:
            if node.key == key: return node.value
        return None
        
    def __iter__(self):
        return ST_unordered_linkedlist.linkedlist_Iterator(self.linked_list)
        
    
    
    def delete(self, key):
        self.put(key, None)
        self.node_count -= 1
        
        
    def contains(self, key):
        return get(key) != null
        
    def isEmpty(self):
        return self.size() == 0
        

    def size(self):
        return self.node_count

def main():
    ST = ST_unordered_linkedlist()
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
    
    for node in ST:
        print('Key:',node.key, 'Value:', node.value)
    
    print(ST.get('Bob'))
    print(ST.get('Ricky'))
    
    
    
    
if __name__=="__main__": main()
        