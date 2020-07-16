# Title: priorityqueue_binaryheap.py
# Author: Ryan Borchardt

# I am implementing the priority queue data structure using a binary heap.
# I am implementing the binary heap data structure using an array (Python list). The binary-heap is 1-indexed (the first node is at a[1]) with a[0] being unused.
# I made the priority queue iterable.
# I am doing this on my own as an exercise.

# Example:
# python priorityqueue_binaryheap.py


class PriorityQueue_BinaryHeap:
    def __init__(self):
        self.h = Binary_Heap()
        
    class _Iterator:
        
        def __init__(self, PQ):
            self.struct = PQ.h.h
            self.max = PQ.h.size()
            self.current_index=1
        
        def __next__(self):
            if self.current_index==self.max+1: raise StopIteration
            returned_item = self.struct[self.current_index]
            self.current_index+=1
            return returned_item
    
    def size(self):
        return self.h.size()
    
    def isEmpty(self):
        return self.h.isEmpty()
    
    def insert(self, v):
        self.h.add_node(v)
    
    def max(self):
        return self.h.max()
    
    def delMax(self):
        return self.h.delMax()
        
    def __iter__(self):
        return PriorityQueue_BinaryHeap._Iterator(self)
        
    
class Binary_Heap:
    def __init__(self):
        self.h = []
        self.number_nodes = 0
        self.h.append(0)
        
    def size(self):
        return self.number_nodes
        
    def isEmpty(self):
        return self.number_nodes==0
    
    # Takes logarithmic time
    def add_node(self, v):
        self.h.append(v)
        self.number_nodes += 1
        # Rearrange the heap so that the newly added node is not violating the heap order.
        self._swim(self.number_nodes)
    
    # Takes constant time
    def max(self):
        return self.h[1]
    
    # Takes logarithmic time        
    def delMax(self):
        # Identify the maximum key in the heap:
        returned_node = self.h[1]
        # Delete this node by replacing it with the node at the end:
        self.h[1] = self.h[self.number_nodes]
        self.h.pop()
        self.number_nodes -= 1
        # Rearrange the heap so that the new root node is not violating the heap order.
        self._sink(1)
        return returned_node
        
    # Takes logarithmic time    
    def _swim(self, i):
        # while (the node isn't moved above being the root node) and (the parent node is less than the child node): 
        while (i>1) and (self.h[i//2] < self.h[i]):
            # since the above condition is true, exchange the parent node with the child node:
            temp = self.h[i//2]
            self.h[i//2] = self.h[i]
            self.h[i] = temp
            # Update the index number so that it is tracking the same node/key across each loop as the key/node swims up 
            i = i//2
            #This loop stops when either 1. the node reaches the root node (the node can swim up no further) or 2. the parent node is not less than the node (the node has found its correct place in the heap).
    
    # Takes logarithmic time
    def _sink(self, i):
        # keep looping as long as the node has children nodes (if it doesn't have children nodes then it has reached the bottom of the heap)
        while 2*i <= self.number_nodes:
            j = 2*i
            # Need to find the greatest child of the node:
            # First need to make sure that the node has two children:
            if j+1 <= self.number_nodes:
                if self.h[j] < self.h[j+1]: j +=1
            # If the node is greater than or equal to the greatest child of the node, then break the loop.
            if self.h[j] <= self.h[i]: break
            # If the node is less than the greatest child of the node, then exchange the nodes:
            else:    
                temp = self.h[i]
                self.h[i] = self.h[j]
                self.h[j] = temp
                # Update the index number so it is tracking the same node/key across each loop as the key/node sinks down.
                i = j
            # This loop stops when either 1. The node reaches the bottom of the heap (2*i >= self.number_nodes) or 2. The node is no longer less than its child nodes (self.h[i] >= self.h[j])


def main():
    PQ = PriorityQueue_BinaryHeap()
    PQ.insert('red')
    PQ.insert('blue')
    
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    PQ.insert('green')
    
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    PQ.insert('yellow')
    
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
        
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

               
        
        
    
    