# Title: st_bst.py
# Author: Ryan Borchardt

# I am implementing an ordered symbol table using an implementation of a binary search tree.
# This symbol table supports ordered operations and is iterable.
# This is an implementation for the ordered symbol table API on page 366 of Sedgewick/Wayne's Algorithms.

# In the worst case (nodes are inserted with in-order or reverse-order keys) the tree height is N.
# In the best case (the tree is perfectly balanced) the tree height is lg(N).
# In the average case (we assume that the nodes are inserted with keys in random order) the average path length is 1.39lg(N) (similar to the mergesort proof).

# Note that I have not yet implemented a way to iterate through a specified range of keys. example: iterate from Buck to Terrance.

# Cost to build full table: ~N*lg(N) (triangular sum approximation) (average case),  ~(N^2)/2 (Stirling's approximation)(worst-case)
# Cost for search hit or update existing key: 1.39*lg(N) (average), N (worst-case)
# Cost to add new key or search miss: 1.39*lg(N) (average), N (worst-case)

# Example:
# python st_bst.py


import sys
sys.path.append('C:/Users/Ryan/Desktop/Work')
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList

class ST_BST:
    def __init__(self):
        self._root = None
        
    class Node:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.node_count = 1
           
        
    def put(self, key, value):
        self._root = self._put(self._root,key,value)
        
    def _put(self,current_node,key,value):
        if current_node == None: return ST_BST.Node(key,value)
        if key == current_node.key: current_node.value = value
        if key < current_node.key: 
            current_node.left = self._put(current_node.left, key, value)
            current_node.node_count = 1 + self.size(current_node.left) + self.size(current_node.right)
        if key > current_node.key: 
            current_node.right = self._put(current_node.right, key, value)
            current_node.node_count = 1 + self.size(current_node.left) + self.size(current_node.right)
        return current_node
        
        
    def get(self, key):
        return self._get(self._root, key)
        
    def _get(self, current_node, key):
        if current_node == None: return None
        if key == current_node.key: return current_node.value
        if key < current_node.key: return self._get(current_node.left, key)
        if key > current_node.key: return self._get(current_node.right, key)

    def contains(self,key):
        return self.get(key) != None
    
    def isEmpty(self):
        return self._root == None
        
    def min(self):
        # Returning the minimum node here, not the key b/c we will use the recursive _min() for other nodes in other operations (see the delete() method)
        minimum_node = self._min(self._root)
        return minimum_node.key

    def _min(self,current_node):
        if current_node.left == None:
            return current_node
        else:
            return self._min(current_node.left)
        
    def max(self):
        maximum_node = self._max(self._root)
        return maximum_node.key
        
    def _max(self, current_node):
        if current_node.right == None:
            return current_node
        else:
            return self._max(current_node.right)
        
    # Python doesn't allow for function overloading (ie can't have multiple different size() methods with different #s of arguments) b/c the local namespace dictionary updates the existing value rather than creating a second entry. 
    # Can use optional arguments to simulate function overloading: if optional_argument=default: do this. if optional_argument != default: do this instead.
    # Can't use instance variables as optional argument b/c at the time of class definition, that instance variable doesn't exist yet
    def size(self,node='special_code'):
        # node='special_code' when no argument is specified
        if node=='special_code': return self._root.node_count
        else:
            if node == None: return 0
            else: return node.node_count
    
    # The floor of a key is the largest key less than the key.
    def floor(self,key):
        node = self._floor(self._root,key)
        if node == None: return None
        return node.key
    
    # The floorkey must satisfy the following two requirements:
    # 1. Be less than (or equal to) the inputted_key
    # 2. Be greater than all of the keys less than the inputted_key
    
    
    def _floor(self,current_node,inputted_key):
        # There are four potential outcomes for the current_node:
        # 1. The current_node == None (ie we didn't find a node that satisfies the two requirements in the subtree)
        # 2. The current_node's key == inputted_key (ie found the floorkey)
        # 3. The current_node's key < inputted_key (ie we might have found the floorkey but requires more investigation)
        # 4. The current_node's key > inputted_key (ie the current_node's key is NOT the floor key and we must move to nodes with smaller keys)
        
        
        
        # 1.
        # If the current_node is None then we didn't find a node with a key that satisfies the two requirements in the subtree
        # Return None to indicate that we didn't find a node that satisfies the two requirements in the subtree
        if current_node == None: return None
       
       
        potential_floorkey = current_node.key
        # 2.
        # If potential_floorkey == inputted_key, we know definitively that the potential_floorkey IS the floorkey b/c it automatically satisfies both of the requirements
        # So we immediately return the node with the floorkey
        if potential_floorkey == inputted_key: return current_node
        
        # 3.
        # If potential_floorkey < inputted_key, we can say that potential_floorkey MIGHT BE the floorkey b/c it satisfies condition 1 but we still don't know if it satisfies condition 2.
        # So we need to investigate to see if there exists a key that is greater than this potential_floorkey that is still less than (or equal to) the inputted_key.
        if potential_floorkey < inputted_key:
            maybe_floorkey_node = current_node
            node_with_biggerkey = current_node.right
            node_with_biggerkey_satisfies_first_requirement = self._floor(node_with_biggerkey, inputted_key)
            # if node_with_biggerkey_satisfies_first_requirement returns None, then we didn't find a Node that satisfies this first requirement and we know that the maybe_floorkey_node is the floorkey:
            if node_with_biggerkey_satisfies_first_requirement == None: return maybe_floorkey_node
            # if node_with_biggerkey_satisfies_first_requirement returns a Node, then we know that this Node is the floorkey:
            if node_with_biggerkey_satisfies_first_requirement != None: return node_with_biggerkey_satisfies_first_requirement
            
        
        # 4.
        # If potential_floor key > inputted_key, we know definitively that potential_floorkey CANNOT be the floorkey (b/c it fails the 1st condition):
        # So we should move to a node with a smaller potential_floorkey:
        if potential_floorkey > inputted_key: return self._floor(current_node.left,inputted_key)


    # The ceiling_key must satisfy the following two requirements:
    # 1. ceiling_key must be greater than (or equal to) the inputted_key
    # 2. ceiling_key must be less than all other keys that are greater than the inputted_key
    
        
    def ceiling(self,key):
        node = self._ceiling(self._root,key)
        if node == None: return None
        return node.key
    
    # The ceiling of a key is the smallest key greater than the key.
    def _ceiling(self,current_node,inputted_key):
        
        # There are four potential outcomes for the current_node:
        # 1. The current_node == None (ie we didn't find a key that satisfies the two requirements)
        # 2. The potential_ceilingkey == inputted_key (ie we automatically know that this potential_ceilingkey IS the ceiling key b/c it automatically satisfies the two requirements)
        # 3. The potential_ceilingkey > inputted_key (ie the potential_ceilingkey MIGHT BE the ceilingkey but requires additional investigation)
        # 4. The potential_ceilingkey < inputted_key (ie the potential_ceilingkey is NOT the ceilingkey and we need to look at node's with smaller keys)
        
        #1.
        if current_node == None: return None
        
        potential_ceilingkey = current_node.key
        #2. 
        if potential_ceilingkey == inputted_key: return current_node
        
        #3.
        if potential_ceilingkey > inputted_key:
            node_with_smaller_key = current_node.left
            node_with_smallerkey_satisfies_first_requirement = self._ceiling(node_with_smaller_key, inputted_key)
            if node_with_smallerkey_satisfies_first_requirement == None: return current_node
            if node_with_smallerkey_satisfies_first_requirement != None: return node_with_smallerkey_satisfies_first_requirement
                
        #4.
        if potential_ceilingkey < inputted_key: return self._ceiling(current_node.right,inputted_key)
        
    # the select() method selects the key with rank k:
    def select(self,k):
        current_node = self._root
        node_rank_k = self._select(self._root,k)
        return node_rank_k.key
        
    def _select(self,current_node,k):
        if current_node == None: return None
        
        left_tree_size = self.size(current_node.left)
        
        #1.
        if left_tree_size == k: return current_node
        
        #2.
        if left_tree_size > k: return self._select(current_node.left,k)
        
        #3.
        if left_tree_size < k: return self._select(current_node.right,k-1-left_tree_size)
        
    # the rank() method outputs the rank of the given key
    def rank(self,key):
        k = self._rank(self._root,key)
        return k
        
    def _rank(self,current_node,key):
        if current_node == None: return 0
        
        #1. 
        if key == current_node.key: return self.size(current_node.left)
        
        #2.
        if key > current_node.key: return  1 + self.size(current_node.left) + self._rank(current_node.right,key)
        
        #3. 
        if key < current_node.key: return self._rank(current_node.left,key)
        
    def deleteMin(self):
        self._root = self._deleteMin(self._root)
        
    def _deleteMin(self, current_node):
        # Find parent of minimum node 
        if current_node.left == None: return current_node.right
        current_node.left = self._deleteMin(current_node.left)
        # Update the node count
        current_node.node_count = 1 + self.size(current_node.left) + self.size(current_node.right)
        return current_node
        
        
    def deleteMax(self):
        self._root = self._deleteMax(self._root)
        
    def _deleteMax(self, current_node):
        if current_node.right == None: return current_node.left
        current_node.right = self._deleteMax(current_node.right)
        current_node.node_count = 1 + self.size(current_node.left) + self.size(current_node.right)
        return current_node
        # Replace parent_node.left = minimum_node.right and update node_counts going back up the tree as the frames are popped off the call stack
        
    def delete(self,key):
        self._root = self._delete(self._root,key)
        
    def _delete(self,current_node,key):
       
        if current_node == None: return None
        
        # Find the node with the key (t):
        if key < current_node.key: 
            current_node.left = self._delete(current_node.left,key)
        elif key > current_node.key: 
            current_node.right = self._delete(current_node.right,key)
        # If key == current_node.key, then we have found the desired node, t:
        else:
            # If the node to be deleted only has one child, then replace this deleted node with its child
            if current_node.left == None: return current_node.right
            if current_node.right == None: return current_node.left
            
            # t is the node to be deleted
            t = current_node
            # Find the smallest node in t.right (x). This replaces the node t b/c: it is greater than all nodes in t.left and it is less than all remaining nodes in t.right. 
            x = self._min(t.right)

            # Assign x.right to the result of t.right.deleteMin()
            # This removes the node X from the subtree and rearranges the subtree to preserve the order
            x.right = self._deleteMin(t.right)
            # Assign x.left to t.left
            x.left = t.left
            # Assign current_node to x 
            current_node = x
        current_node.node_count = 1 + self.size(current_node.left) + self.size(current_node.right)
        return current_node
        
        
        
    class _Iterator:
        def __init__(self,root_node):
            self.root_node = root_node
            self.current_node = root_node
            self.queue = Queue_LinkedList()
            
            # Build the queue (default is from least node to greatest node)
            self.build_queue(self.current_node)
            
            
        def __next__(self):
            if self.queue.isEmpty() == True: raise StopIteration
            returned_node = self.queue.dequeue()
            return returned_node
            
        def build_queue(self,current_node):
            if current_node == None: return
            self.build_queue(current_node.left)
            self.queue.enqueue(current_node)
            #print(current_node.key)
            self.build_queue(current_node.right)

    def __iter__(self):
        return ST_BST._Iterator(self._root)
        
        


def main():
    ST = ST_BST()
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
    
    
    print(ST.get('Bill'))
    print(ST.get('George'))
    print(ST.get('Tom'))
    print(ST.isEmpty())
    print(ST.contains('Terrance'))
    print('minimum:', ST.min())
    print(ST.max())
    print(ST.size())
    
    print(ST.floor('Craig'))
    print(ST.ceiling('Craig'))
    print(ST.ceiling('Roger'))
    
    print(ST.select(3))
    print(ST.select(5))
    
    
    print(ST.rank('Bill'))
    print(ST.rank('Ricky'))
    
    ST.deleteMin()
    ST.deleteMax()
    ST.delete('Howard')
    
    # Re-add the nodes deleted previously:
    ST.put('Bill', 55)
    ST.put('Tom', 24)
    ST.put('Howard', 31)
    
    print('Iterating through BST in order:\n')
    for i in ST:
        print(i.key)


if __name__=="__main__": main()        