
# 12/17/2020 implementation of BST for all methods in API on page ___.

# python bst_new.py


import sys
from chapter_1.queue.queue_linkedlist import Queue_LinkedList
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.node_count = 1
        self.left = None
        self.right = None 
        

class BST:
    def __init__(self):
        self.root = None
        
    def get(self, key):
        node = self._get(self.root,key)
        if node is None:
            return None
        elif node is not None:
            return node.value
            
    def _get(self,current_node,key):
        if current_node is None:
            return None
        
        elif key > current_node.key:
            return self._get(current_node.right, key)
        
        elif key < current_node.key:
            return self._get(current_node.left, key)
            
        else: #key == current_node.key
            return current_node
            
    def put(self, key, value):
        self.root = self._put(self.root,key,value)
    
    def _put(self,current_node,key,value):
        if current_node is None:
            return Node(key,value)
        
        elif key > current_node.key:
            current_node.right = self._put(current_node.right,key,value)
            current_node.node_count = 1 + self.size(current_node.left) + self.size(current_node.right)
            return current_node
        
        elif key < current_node.key:
            current_node.left = self._put(current_node.left,key,value)
            current_node.node_count = 1 + self.size(current_node.left) + self.size(current_node.right)
            return current_node
            
        else: # key == current_node.key:
            current_node.value = value
            current_node.node_count = 1 + self.size(current_node.left) + self.size(current_node.right)
            return current_node
    
    # This method serves as two methods:
        #1. if called with no arguments, returns size of entire tree
        #2. if called with arguments, returns size of specific node
    def size(self, current_node='default'):
        if current_node=='default':
            return self.root.node_count
        
        else:
            if current_node is None:
                return 0
            else:
                return current_node.node_count
                
                
    def isEmpty(self):
        return self.size()==0
        
    def contains(self, key):
        return self.get(key) is not None
        
    # Iterative version (works, tested)
    #def min(self):
    #    current_node = self.root
    #    while current_node.left is not None:
    #        current_node = current_node.left
    #    return current_node.key 
        
    # recursive version
    def min(self):
        if self.root is None:
            return None
        else:
            node = self._min(self.root)
            return node.key
            
    def _min(self,current_node):
        if current_node.left is None:
            return current_node
        else:
            return self._min(current_node.left)
            
            
    def max(self):
        if self.root is None:
            return None
        else:
            node = self._max(self.root)
            return node.key
    
    def _max(self,current_node):
        if current_node.right is None:
            return current_node
        else:
            return self._max(current_node.right)
            
            
    def floor(self, key):
        node = self._floor(self.root,key)
        if node is None:
            return None
        else:
            return node.key
        
    def _floor(self,current_node,key):
        if current_node is None:
            return None 
        
        potential_floorkey = current_node.key
        
        if potential_floorkey < key:
            # then potential_floorkey MIGHT be the floorkey b/c it satisifies the first condition that floorkey is <= key. need to check and see if it is greatest key that is <= key
            maybe_floorkey_node = self._floor(current_node.right,key)
            if maybe_floorkey_node is None: 
                return current_node
            else:
                return maybe_floorkey_node
        
        elif potential_floorkey > key:
            # then potential_floorkey is NOT the floorkey, need to search left subtree
            return self._floor(current_node.left,key)
            
        else: # potential_floorkey == key:
            # then potential_floorkey is the floor key
            return current_node
        
        
    def ceiling(self,key):
        node = self._ceiling(self.root,key)
        if node is None:
            return None
        else:
            return node.key
    
    def _ceiling(self,current_node,key):
        if current_node is None:
            return None
        
        potential_ceilkey = current_node.key
        
        if potential_ceilkey == key:
            return current_node
        
        # potential_ceilkey MIGHT be the real ceiling key. it satisifies the first condition. need to see if it passes the second
            # 1. ceiling key must be greater than or equal to key (passes)
            # 2. ceiling key must be the least of all keys greater than key: need to see if there exists a key in the left subtree that is still greater than key 
        elif potential_ceilkey > key:
            maybe_ceilkey_node = self._ceiling(current_node.left ,key)
            if maybe_ceilkey_node is None:
                return current_node
            else:
                return maybe_ceilkey_node 
                
        else: # if potentia_ceilkey < key 
            # if this is true, we know that potential_ceilkey is NOT the ceiling key. need to look in right subtree for bigger potential ceiling keys
            return self._ceiling(current_node.right,key)
    
    
    # rank() returns the # of keys less than key
    def rank(self, key):
        if self.root is None:
            return None
        else:
            return self._rank(self.root, key)
            
    def _rank(self,current_node,key):
        if current_node is None:
            return 0
        
        elif current_node.key < key:
            return self.size(current_node.left) + 1 + self._rank(current_node.right, key)
            
        elif current_node.key >= key:
            return 0 + self._rank(current_node.left, key)
        
        
       
    def select(self, r):
        node = self._select(self.root,r)
        if node is None:
            return None
        else:
            return node.key
            
    def _select(self,current_node,r):
        # reminder that self.size(None) = 0
        if self.size(current_node.left) < r:
            return self._select(current_node.right, r-self.size(current_node.left)-1)
        
        elif self.size(current_node.left) > r:
            return self._select(current_node.left, r)
        
        else: # self.size(current_node.left) == r
            return current_node
    # lo_key and hi_key don't have to be keys in symbol table
    def range_size(self,lo_key,hi_key): # inclusive on both ends
        real_lo = self.ceiling(lo_key)
        real_hi = self.floor(hi_key)
        return self.rank(real_hi)-self.rank(real_lo) + 1
        
        
    def __iter__(self):
        # how do you call a nested class??
        return BST.BST_Iterator(self.root) #iterator object

    class BST_Iterator:
        def __init__(self, root):
            self.queue = Queue_LinkedList()
            
            self.build_queue(root)
            
        def build_queue(self,current_node):
            if current_node is None:
                return
            
            self.build_queue(current_node.left)
            self.queue.enqueue(current_node)
            self.build_queue(current_node.right)
        
        
        
        def __next__(self):
            if self.queue.isEmpty() is True:
                raise StopIteration
            else:
                return self.queue.dequeue().key
                
    def deleteMin(self):
        self.root = self._deleteMin(self.root)
        
    def _deleteMin(self,current_node):
        if current_node.left is None:
            return current_node.right
        else:
            current_node.left = self._deleteMin(current_node.left)
            return current_node
    
    def deleteMax(self):
        self.root = self._deleteMax(self.root)
        
    def _deleteMax(self,current_node):
        if current_node.right is None:
            return current_node.left 
        else:
            current_node.right = self._deleteMax(current_node.right)
            return current_node
            
            
    def delete(self,key):
        self.root = self._delete(self.root,key)
        
    def _delete(self,current_node,key):
        
        if key < current_node.key:
            current_node.left = self._delete(current_node.left,key)
            return current_node
        
        elif key == current_node.key:
            x = self._min(current_node.right)
            self._deleteMin(current_node.right)
            x.right = current_node.right
            x.left = current_node.left
            return x
            
        else: # key > current_node.key 
            current_node.right = self._delete(current_node.right,key)
            return current_node
            
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,value):
        self.put(key,value)

def main():
    ST = BST()
    ST.put('M', 24)
    ST.put('R', 55)
    ST.put('T', 78)
    ST.put('W', 12)
    ST.put('S', 43)
    ST.put('P', 23)
    ST.put('O', 31)
    ST.put('Q', 94)
    ST.put('F', 19)
    ST.put('D', 61)
    ST.put('H', 71)
    ST.put('A', 23)
    ST.put('E', 39)
    ST.put('G', 16)
    ST.put('K', 64)
    
    
    print(ST.get('P'))
    print(ST.size())
    print(ST.isEmpty())
    print(ST.contains('W'))
    print(ST.contains('Z'))
    print(ST.min())
    print(ST.max())
    print(ST.floor('N')) # M
    print(ST.floor('I')) # H
    print(ST.ceiling('N')) # O
    print(ST.ceiling('I')) # K
    
    print(ST.rank('N')) # 8
    print(ST.rank('V')) # 8 + 4 + 2 + 0 = 14
    print(ST.rank('B')) # 1
    print('R rank',ST.rank('R')) # 11
    print(ST.rank('W')) # 14
    
    print(ST.select(9)) # P
    print(ST.select(0)) # A
    
    print(ST.range_size('R','W')) # 4
    print(ST.range_size('R','Z')) # 4
 
    for key in ST:
        print(key)
        
    #print('min')
    #print(ST.min())
    #ST.deleteMin()
    #print(ST.min())
    
    
    #print('max')
    #ST.deleteMax()
    #print(ST.max())
    #ST.deleteMax()
    #print(ST.max())
    
    
    ST.delete('F')
    
    for key in ST:
        print(key)
        
    print(ST['H'])
    
    ST['Z']=3
   

if __name__=="__main__": main()        