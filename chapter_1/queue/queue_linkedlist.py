# Title: queue_linkedlist.py
# Author: Ryan Borchardt

# I am implementing the queue data structure using an implementation of linked lists.
# For this implementation: push() inserts node to end of linked list and pop() removes first node from linked list. 
# Requires additional instance variable to reference the last node in linked list to avoid having to traverse linked list
# I made the queue iterable.

# Example:
# python queue_linkedlist.py < tobe.txt

import sys

class Queue_LinkedList:
    def __init__(self):
        self._first_node = None
        self._node_count = 0
        self._last_node = None
        
        
    class _Node:
        def __init__(self, item):
            self.item = item
            self.next = None
            
    class _Iterator_Queue_LinkedList:
        def __init__(self, queue):
            self.current_node = queue._first_node
        
        def __next__(self):
            if self.current_node == None: raise StopIteration
            returned_item = self.current_node.item
            self.current_node = self.current_node.next
            return returned_item
        
    def __len__(self):
        return self._node_count
    
    def isEmpty(self):
        return self._node_count==0
    
    def enqueue(self, item):
        new_node = Queue_LinkedList._Node(item)
        if self._node_count == 0:
            self._first_node = new_node
            self._last_node = new_node
        else:
            self._last_node.next = new_node
            self._last_node = new_node
        
        self._node_count += 1
    
    def dequeue(self):
        returned_item = self._first_node.item
        self._first_node = self._first_node.next
        self._node_count -= 1
        return returned_item
    
    def __iter__(self):
        return Queue_LinkedList._Iterator_Queue_LinkedList(self)
    
    
def main():
    queue = Queue_LinkedList()
    print(len(queue))
    print(queue.isEmpty())
    
    queue.enqueue('red')
    queue.enqueue('green')
    queue.enqueue('blue')
    queue.enqueue('yellow')
    
    print(len(queue))
    print(queue.isEmpty())
    
    print(queue.dequeue())
    print(queue.dequeue())
    
    print(len(queue))
    
    queue.enqueue('purple')
    queue.enqueue('orange')
    queue.enqueue('brown')
    
    for item in queue:
        print(item)
        
    print('-------')
        
    queue_2 = Queue_LinkedList()
    data = sys.stdin.readline()
    list_word_strings = data.split(" ")
    
    for word in list_word_strings:
        if word == "-":
            sys.stdout.write(str(queue_2.dequeue()) + " \n")
        else:
            queue_2.enqueue(word)
    summary_string = "(" + str(len(queue_2)) + " left on queue)."
    sys.stdout.write(summary_string)
        
if __name__=="__main__": main()        
     
    
    