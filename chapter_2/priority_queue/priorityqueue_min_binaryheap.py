# Title: priorityqueue_min_binaryheap.py
# Author: Ryan Borchardt

# I am implementing a minimum priority queue data structure using a binary heap.

# The only functional difference in the implementation between the minimum priority queue and the maximum priority queue is the implementation of the _sink() and _swim() methods.

# I am implementing the binary heap data structure using an array (Python list). The binary-heap is 1-indexed (the first node is at a[1]) with a[0] being unused.
# I made the priority queue iterable.

# Example:
# python priorityqueue_min_binaryheap.py


class PriorityQueue_Min_BinaryHeap:
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
    
    def min(self):
        return self.h.min()
    
    def delMin(self):
        return self.h.delMin()
    
    def __len__(self):
        return self.h.size()
        
    def __iter__(self):
        return PriorityQueue_Min_BinaryHeap._Iterator(self)
        
    
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
    def min(self):
        return self.h[1]
    
    # Takes logarithmic time        
    def delMin(self):
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
        # Boundary Case #1: If this is true, then the binary heap only has one element and _swim() doesn't need to run
        if i == 1:
            return
        
        parent_node_index = i//2
        parent_node = self.h[parent_node_index]
        i_node = self.h[i]
        
        while parent_node >= i_node:
            # Exchange the parent_node and i_node
            self.h[parent_node_index] = i_node
            self.h[i] = parent_node

            #Re-assign
            i = parent_node_index
            parent_node_index = i//2
            
            i_node = self.h[i]
            parent_node = self.h[parent_node_index]
            
            # Boundary Case 2: If this is true, we have reached the top of the binary heap and _swim() can stop running
            if i == 1:
                return
            

    # Takes logarithmic time
    def _sink(self, i):
        if self.number_nodes ==0:
            return
        i_node = self.h[i]
        
        child_node_1_index = i*2
        child_node_2_index = i*2+1
        
        # Boundary Case 1:
        # if this is true, the node can sink no lower b/c it has no children
        if self.number_nodes < child_node_1_index:
            return
        
        # Boundary Case 2:
        # If the above was not true but this is true, then the node only has one child and that child is automatically the least_child
        elif self.number_nodes < child_node_2_index:
            least_child_index = child_node_1_index
            least_child_node = self.h[child_node_1_index]
        
        # Typical case.
        else:
            if self.h[child_node_1_index] <= self.h[child_node_2_index]:
                least_child_index = child_node_1_index
                least_child_node = self.h[child_node_1_index]
            else:
                least_child_index = child_node_2_index
                least_child_node = self.h[child_node_2_index]            
        
        while i_node >= least_child_node:
            # Exchange i_node and least_child_node
            self.h[i] = least_child_node
            self.h[least_child_index] = i_node
            
            # Re-assign:
            i = least_child_index
            i_node = self.h[i]
            
            child_node_1_index = i*2
            child_node_2_index = i*2+1
        
            # Boundary Case 1:
            # if this is true, the node can sink no lower b/c it has no children
            if self.number_nodes < child_node_1_index:
                return
        
            # Boundary Case 2:
            # If the above was not true but this is true, then the node only has one child and that child is automatically the least_child
            elif self.number_nodes < child_node_2_index:
                least_child_index = child_node_1_index
                least_child_node = self.h[child_node_1_index]
        
            # Typical case.
            else:
                if self.h[child_node_1_index] <= self.h[child_node_2_index]:
                    least_child_index = child_node_1_index
                    least_child_node = self.h[child_node_1_index]
                else:
                    least_child_index = child_node_2_index
                    least_child_node = self.h[child_node_2_index]   
            
            


def main():
    PQ = PriorityQueue_Min_BinaryHeap()
   
    

    # Lets say we are dealing with distances from s to vertices v:
    # This priority queue removes the min distance in lg(N) time and inserts an edge-weight in lg(N) time.
    # These edge weights were taken from tinyEWD.txt
    PQ.insert(0.35)
    PQ.insert(0.35)
    
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    PQ.insert(0.37)
    PQ.insert(0.28)
    PQ.insert(0.28)
    PQ.insert(0.32)
    PQ.insert(0.38)
    
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    PQ.insert(0.26)
    PQ.insert(0.39)
    PQ.insert(0.29)
    PQ.insert(0.34)
    
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    PQ.insert(0.40)
    PQ.insert(0.52)
    PQ.insert(0.58)
    
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    PQ.insert(0.93)
    
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    
    
    print('Deleted minimum: ', PQ.delMin())
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    print('Deleted minimum: ', PQ.delMin())
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    print('Deleted minimum: ', PQ.delMin())
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    print('Deleted minimum: ', PQ.delMin())
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    print('Deleted minimum: ', PQ.delMin())
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')
    
    print('Deleted minimum: ', PQ.delMin())
    print('Priority Queue:')
    for i in PQ:
        print(i)
    print('Size: ', PQ.size())
    print('\n')    
    
    


if __name__=="__main__": main()

               
        
        
    
    