# Title: priorityqueue_unorderedlinkedlist.py
# Author: Ryan Borchardt

# I am implementing the priority queue data structure using a linked list that I structure to be unordered.
# I made the priority queue iterable.
# I am doing this on my own as an exercise.

# Example:
# python priorityqueue_unorderedlinkedlist.py

class PriorityQueue_UnorderedLinkedList:
    def __init__(self):
        self.linked_list = None
        self.node_count = 0
        
    class _Iterator:
        def __init__(self,PQ_object):
            self.current_node = PQ_object.linked_list
            self.node_count = PQ_object.node_count
            
        def __next__(self):
            if self.current_node == None: raise StopIteration
            returned_item = self.current_node.item
            self.current_node = self.current_node.next
            return returned_item
    
    class _Node:
        def __init__(self,item):
            self.item = item
            self.next = None
    
    def size(self):
        return self.node_count
    
    def isEmpty():
        return self.node_count==0
    
    # Constant time
    def insert(self, v):
        new_node = PriorityQueue_UnorderedLinkedList._Node(v)
        new_node.next = self.linked_list
        self.linked_list = new_node
        self.node_count +=1
    
    # Linear time: Need to iterate through each node of the linked list and check to see if that node's item is greater than the current maximum item.
    
    def max(self):
        current_max_node = self.linked_list
        node_before_max = None
        current_node = self.linked_list.next
        current_previous_node = self.linked_list
        
        
        for i in range(1,self.node_count):
            if current_node.item > current_max_node.item:
                current_max_node = current_node
                node_before_max = current_previous_node

            current_node = current_node.next
            current_previous_node = current_previous_node.next
        
        return current_max_node.item
            
    
    
    # Linear time:
    # 1. Find node with maximum item (linear time)
    # 2. Resassign the previous node's next attribute to the node after the node with the maximum item (constant time)
    #   Could make the linkedlist into a doubly linked list to make this simpler.

    
    def delMax(self):
        current_max_node = self.linked_list
        node_before_max = None
        current_node = self.linked_list.next
        current_previous_node = self.linked_list
        
        
        for i in range(1,self.node_count):
            if current_node.item > current_max_node.item:
                current_max_node = current_node
                node_before_max = current_previous_node
            
            current_node = current_node.next
            current_previous_node = current_previous_node.next
        
        # Reassign previous node's next attribute to the node after the max node to cut out the max node
        
        # If the max node is the first node in the linked list, the node_before_max is  None
        if node_before_max == None:
            self.linked_list = current_max_node.next
            self.node_count -= 1
        else:
            node_before_max.next = current_max_node.next
            self.node_count -= 1
        
        return current_max_node.item
        
        
    def __iter__(self):
        return PriorityQueue_UnorderedLinkedList._Iterator(self)

def main():
    PQ = PriorityQueue_UnorderedLinkedList()
    PQ.insert('red')
    PQ.insert('blue')
    PQ.insert('green')
    PQ.insert('yellow')
    PQ.insert('brown')
    PQ.insert('grey')
    
    # I made the priority queue iterable
    print('Priority Queue:')
    for i in PQ:
        print(i)

    print('Size: ', PQ.size())
    print('\n')    
    
    print('Deleted maximum: ', PQ.delMax())
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    print('Deleted maximum: ', PQ.delMax())
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    print('Deleted maximum: ', PQ.delMax())
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    print('Deleted maximum: ', PQ.delMax())
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    print('Deleted maximum: ', PQ.delMax())
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    print('Deleted maximum: ', PQ.delMax())
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')    



if __name__=="__main__": main()