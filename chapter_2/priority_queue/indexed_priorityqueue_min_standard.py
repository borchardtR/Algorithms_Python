# Title: indexed_priorityqueue_min_standard.py
# Author: Ryan Borchardt

"""
For the standard implementation of indexed priority queues, the index is restricted to being consecutive integers from 0 to max_nodes-1.
See my implementation: indexed_priorityqueue_min_custom.py if customization of the index is desired.

I wrote an explanation of how an indexed priority queue works and why it is useful b/c in my opinion the book doesn't do an adequate job on this one subject
See Indexed_Priority_Queue_Explanation.pdf

Implementation of API on page 320.

For indexed priority queues, "keys" are priority levels and determine the position of its corresponding index in the priority queue. 
The keys can be any comparable object. 

For indexed priority queues, "indices" are integers from 0 to max_nodes-1 and are paired with a key. They are used to dynamically change or delete a key from a priority queue.
For the standard implementation of indexed priority queues, the index is restricted to being consecutive integers from 0 to max_nodes-1.

The self.qp array is used as an inverted index. Given an index, self.qp can be used to determine its position in the priority queue.

In this implementation, a binary heap data structure is used for self.pq but the binary heap data structure is not explicitly defined as a separate class.
Requires max_size to be stated when Index_PriorityQueue_Min object is created (not dynamic).

Example use of this data structure is for graphs: Djikstra's algorithm
    The index (0 through max_nodes-1) correspond to to the vertices
    The keys correspond to their distance from the source vertex
    We can dynamically change the distance from the source vertex for a given vertex: The below code changes the vertex 2 to have a distance of 0.1
    iPQ.change(2, 0.1)
    We can answer questions like the following:
        Q1: What is the 2nd smallest distance? 
        A1: self.pq[2] = 7, keys[7] = 0.42. The second smallest distance is 0.42, which is for vertex 7.
        Q2: Where is vertex 6 on the priority queue?
        A2: self.qp[6] = 7. Vertex 6 is the 7th vertex on the priority queue.
        Q3. Update the distance for vertex 4 to 0.57?
        A3: (decreasing key) keys[4] = 0.57, qp[4] = 5 so _swim(5)
        Q4: Increase the distance for vertex 1 to 2.5?
        A4: keys[1] = 2.5, _sink(qp[1]=4)
        

Indexed priority queues allow for:
1. Changing the prioirty of an index (vertex) in lg() time
2. Associating an index with each priority level 


"""
# Example:
# python indexed_priorityqueue_min_standard.py


class Indexed_PriorityQueue_Min:
    def __init__(self, max_nodes):
        # 
        self.pq = [None]*(max_nodes+1)
        self.keys = [None]*(max_nodes)
        self.qp = [None]*(max_nodes+1)
        self.node_count = 0
        self.max_nodes = max_nodes
    
    # Returns tuple(index, key) pairs 
    # Does NOT iterate from low key to high key
    class _Iterator:
        
        def __init__(self, indexed_minPQ):
            self.pq = indexed_minPQ.pq
            self.keys = indexed_minPQ.keys
            
            self.size = indexed_minPQ.size()
            self.current_pqindex=1
        
        def __next__(self):
            if self.current_pqindex==self.size+1: raise StopIteration
            returned_index = self.pq[self.current_pqindex]
            returned_key = self.keys[returned_index]
            self.current_pqindex+=1
            return (returned_index, returned_key)
    
    def size(self):
        return self.node_count
    
    def isEmpty(self):
        return self.node_count==0
    
    def insert(self, index, key):
        self.keys[index] = key
        
        self.pq[self.node_count+1] = index
        self.qp[index] = self.node_count+1
        
        self._swim(self.node_count+1)
        self.node_count +=1
        # self.qp is updated in the _swim() operation
        
        
    
    # Takes in an index value and returns True if the index is in the indexed_priority_queue
    def contains(self, index):
        return self.qp[index] != None
    
    # Change the current_key associated with an index value to key
    def change(self, index, key):
        current_key = self.keys[index]
        
        current_pqindex = self.qp[index]
        
        if current_key > key:
            self.keys[index] = key
            self._swim(current_pqindex)
        else:
            self.keys[index] = key
            self._sink(current_pqindex)
            
    # Delete the specified index and its corresponding key
    def delete(self, index):
        self.keys[index] = None
        pqindex = self.qp[index]
        self.pq[pqindex] = self.pq[self.node_count]
        self.pq[self.node_count] = None
        self.qp[index] = None
        self.node_count -= 1
        self._sink(1)
    
    # Returns the index with the smallest priority level / smallest key value
    def minIndex(self):
        index = self.pq[1]
        key = self.keys[index]
        return index
        
    # Returns the smallest priority level / smallest key value
    def min(self):
        index = self.pq[1]
        key = self.keys[index]
        return key
    
    # Returns the index with the smallest priority level / smallest key value
    # Deletes the smallest key value and its correspoding index (from self.keys, self.pq and self.qp)
    def delMin(self):
        index = self.pq[1]
        key = self.keys[index]
        
        # Delete this node by replacing it with node at end of priority queue
        self.pq[1] = self.pq[self.node_count]
        self.pq[self.node_count] = None
        
        self.qp[index] = None
        
        #self.node_count -= 1
        self.node_count -= 1
        self._sink(1)
        #self.node_count -= 1
        # Remove key
        self.keys[index] = None
        return index


    
    def __iter__(self):
        return Indexed_PriorityQueue_Min._Iterator(self)
        
    
    def _swim(self, i_node_pqindex):
        # Boundary Case #1: If this is true, then the binary heap only has one element and _swim() doesn't need to run
        if i_node_pqindex == 1:
            return
        
        parent_node_pqindex = i_node_pqindex//2
        parent_node_index = self.pq[parent_node_pqindex]
        parent_node_key = self.keys[parent_node_index]
       
        i_node_index = self.pq[i_node_pqindex]
        i_node_key = self.keys[i_node_index]
        while parent_node_key >= i_node_key:
            # Exchange the parent_node_index and i_node_index in the priority queue:
            self.pq[i_node_pqindex] = parent_node_index
            self.pq[parent_node_pqindex] = i_node_index
            
            # Exchange the nodes in the inverted index:
            self.qp[i_node_index] = parent_node_pqindex
            self.qp[parent_node_index] = i_node_pqindex

            #Re-assign
            i_node_pqindex = parent_node_pqindex           
            
            # Boundary Case 2: If this is true, we have reached the top of the binary heap and _swim() can stop running
            if i_node_pqindex == 1:
                return
                
            # i_node_index and i_node_key stay the same.
            parent_node_pqindex = i_node_pqindex//2
            parent_node_index = self.pq[parent_node_pqindex]
            parent_node_key = self.keys[parent_node_index] 
                
                
    def _sink(self, i_node_pqindex):
        if self.node_count == 0:
            return
        
        i_node_index = self.pq[i_node_pqindex]
        i_node_key = self.keys[i_node_index]
        
        child_node_1_pqindex = i_node_pqindex*2

        
        child_node_2_pqindex = i_node_pqindex*2+1
   
        # Boundary Case 1:
        # if this is true, the node can sink no lower b/c it has no children
        if self.node_count < child_node_1_pqindex:
            return
        
        # Boundary Case 2:
        # If the above was not true but this is true, then the node only has one child and that child is automatically the least_child
        elif self.node_count < child_node_2_pqindex:
            least_child_node_pqindex = child_node_1_pqindex
            least_child_node_index = self.pq[child_node_1_pqindex]
            least_child_node_key = self.keys[least_child_node_index]
        
        # Typical case.
        else:
            child_node_1_index = self.pq[child_node_1_pqindex]
            child_node_1_key = self.keys[child_node_1_index]
            child_node_2_index = self.pq[child_node_2_pqindex]
            child_node_2_key = self.keys[child_node_2_index]
            
            if child_node_1_key <= child_node_2_key:
                least_child_node_pqindex = child_node_1_pqindex
                least_child_node_index = child_node_1_index
                least_child_node_key = child_node_1_key
            else:
                least_child_node_pqindex = child_node_2_pqindex
                least_child_node_index = child_node_2_index
                least_child_node_key = child_node_2_key           
        
        while i_node_key >= least_child_node_key:
            
            # Exchange the least_child_node_index and i_node_index in the priority queue:
            self.pq[i_node_pqindex] = least_child_node_index
            self.pq[least_child_node_pqindex] = i_node_index
            
            # Exchange the nodes in the inverted index... this is wrong....:
            self.qp[i_node_index] = least_child_node_pqindex
            self.qp[least_child_node_index] = i_node_pqindex
            
            #Re-assign
            i_node_pqindex = least_child_node_pqindex
            # i_node_index and i_node_key stay the same.
            child_node_1_pqindex = i_node_pqindex*2
            #child_node_1_index = self.pq[child_node_1_pqindex]
            #child_node_1_key = self.keys[child_node_1_index]
        
            child_node_2_pqindex = i_node_pqindex*2+1
            #child_node_2_index = self.pq[child_node_2_pqindex]
            #child_node_2_key = self.keys[child_node_2_index] 
             
        
            # Boundary Case 1:
            # if this is true, the node can sink no lower b/c it has no children
            if self.node_count < child_node_1_pqindex:
                return
        
            # Boundary Case 2:
            # If the above was not true but this is true, then the node only has one child and that child is automatically the least_child
            elif self.node_count < child_node_2_pqindex:
                least_child_node_pqindex = child_node_1_pqindex
                least_child_node_index = self.pq[child_node_1_pqindex]
                least_child_node_key = self.keys[least_child_node_index]
        
            # Typical case.
            else:
                child_node_1_index = self.pq[child_node_1_pqindex]
                child_node_1_key = self.keys[child_node_1_index]
                child_node_2_index = self.pq[child_node_2_pqindex]
                child_node_2_key = self.keys[child_node_2_index]
            
                if child_node_1_key <= child_node_2_key:
                    least_child_node_pqindex = child_node_1_pqindex
                    least_child_node_index = child_node_1_index
                    least_child_node_key = child_node_1_key
                else:
                    least_child_node_pqindex = child_node_2_pqindex
                    least_child_node_index = child_node_2_index
                    least_child_node_key = child_node_2_key             
            
            


def main():
    iPQ = Indexed_PriorityQueue_Min(8)

    iPQ.insert(0,0)
    iPQ.insert(1,0.79)
    iPQ.insert(2,1.42)
    iPQ.insert(3,float('inf'))
    iPQ.insert(4, 1.32)
    
    iPQ.insert(5, 0.46)
    iPQ.insert(6, float('inf'))
    iPQ.insert(7, 0.42)
    
    print(iPQ.keys)
    print(iPQ.pq)
    print(iPQ.qp)
    
    for i in iPQ:
        print(i)
    
    print('\n')
    print(iPQ.delMin())
    print(iPQ.keys)
    print(iPQ.pq)
    print(iPQ.qp)
    for i in iPQ:
        print(i)    
    
    
    print('\n')
    iPQ.delete(5)
    for i in iPQ:
        print(i)

    print(iPQ.contains(4))
    print(iPQ.contains(5))
    print(iPQ.min())

    
    iPQ.change(2, 0.1)
    print('\n')
    print(iPQ.keys)
    print(iPQ.pq)
    print(iPQ.qp)
    for i in iPQ:
        print(i) 
    

if __name__=="__main__": main()

               
        
        
    
    