# Title: linkedlistbag.py
# Date: 5/25/2020
# Author: Ryan Borchardt
# I am implementing the bag data structure using an implementation of linked lists.
# I made the bag iterable (the order of iteration doesn't matter for bags so I chose to traverse it in the order: LIFO. 
import sys

class LinkedListBag:
    def __init__(self):
        self._linked_list = None
        self._node_count = 0
        
        
    class _Node:
        def __init__(self, item):
            self.item = item
            self.next = None
            
    class _Iterator_LinkedListBag:
        def __init__(self, bag):
            self.current_node = bag._linked_list
        
        def __next__(self):
            if self.current_node == None: raise StopIteration
            returned_item = self.current_node.item
            self.current_node = self.current_node.next
            return returned_item
        
    def __len__(self):
        return self._node_count
    
    def isEmpty(self):
        return self._node_count==0
    
    def add(self, item):
        old_first_node = self._linked_list
        new_node = LinkedListBag._Node(item)
        new_node.next = old_first_node
        self._node_count += 1
        self._linked_list = new_node
   
    
    def __iter__(self):
        return LinkedListBag._Iterator_LinkedListBag(self)
    
    
def main():
    bag = LinkedListBag()
    print(len(bag))
    print(bag.isEmpty())
    
    bag.add('red')
    bag.add('green')
    bag.add('blue')
    bag.add('yellow')
    
    print(len(bag))

    bag.add('purple')
    bag.add('orange')
    bag.add('brown')
    
    for item in bag:
        print(item)
        
        
if __name__=="__main__": main()        
     
    
    
        