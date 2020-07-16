# Title: priorityqueue_orderedlinkedlist.py
# Author: Ryan Borchardt

# I am implementing the priority queue data structure using a linked list that I structure to be ordered.
# I made the priority queue iterable.
# I am doing this on my own as an exercise.

# Example:
# python priorityqueue_orderedlinkedlist.py

class PriorityQueue_OrderedLinkedList:
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
    
    #Takes linear time 
    def insert(self, v):
        new_node = PriorityQueue_OrderedLinkedList._Node(v)
        current_node = self.linked_list
        previous_node = None
        not_last_node = False
        if self.node_count == 0:
            self.linked_list = new_node           
            self.node_count += 1
            return
        
        for i in range(0,self.node_count):
            if v >= current_node.item:
                # If the new item is greater than all of the items, the new node will be the first node:
                if i==0:
                    new_node.next = self.linked_list
                    self.linked_list = new_node
                else:
                    previous_node.next = new_node
                    new_node.next = current_node
                not_last_node=True
                self.node_count += 1
                break

            previous_node = current_node
            current_node = current_node.next
            
        if not_last_node == False:
            # Assign previous_node.next to new_node b/c at this point, current_node = None
            previous_node.next=new_node
            self.node_count +=1
            
    

    # Takes constant time
    def max(self):
        returned_item = self.linked_list.item
        return returned_item



    # Takes constant time
    def delMax(self):
        returned_item = self.linked_list.item
        self.linked_list = self.linked_list.next
        self.node_count -= 1
        return returned_item
        
    def __iter__(self):
        return PriorityQueue_OrderedLinkedList._Iterator(self)

def main():
    PQ = PriorityQueue_OrderedLinkedList()
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