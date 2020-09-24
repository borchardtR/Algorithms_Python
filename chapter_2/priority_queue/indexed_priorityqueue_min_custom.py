# Title: indexed_priorityqueue_min_custom.py
# Author: Ryan Borchardt

"""
For the custom implementation of indexed priority queues, the index can be any data type that is hashable.
See my implementation: indexed_priorityqueue_min_standard.py if standard verticies from 0 to max_nodes-1 is desired.

I wrote an explanation of how an indexed priority queue works and why it is useful b/c in my opinion the book doesn't do an adequate job on this one subject
See Indexed_Priority_Queue_Explanation.pdf

Implementation of API on page 320.

For indexed priority queues, "keys" are priority levels and determine the position of its corresponding index in the priority queue. 
The keys can be any comparable object. 

For custom indexed priority queues, "indices" are objects that are paired with a key. They are used to dynamically change or delete a key from a priority queue.

The self.qp hash table is used as an inverted index. Given an index, self.qp can be used to determine its position in the priority queue.

In this implementation, a binary heap data structure is used for self.pq but the binary heap data structure is not explicitly defined as a separate class.
A max_size is not required to be stated when Index_PriorityQueue_Min object is created.

Example use of this data structure is for hospitals:
    The indices correspond to the names of the patients.
    The keys correspond to their health score. Patients are seen in the order from lowest health score to highest health score.
    We can dynamically change the health score of a given patient (if it changes while they are waiting for instance): The below code changes the index "Pete" to have a health score of 1.
    iPQ.change("Pete", 1)
    We can answer questions like the following:
        Q1: What is the 2nd lowest health score? 
        A1: self.pq[2] = "Billy", keys["Billy"] = 2. The second lowest health score is 2, which is for patient "Billy".
        Q2: Where is "Steve" on the priority queue?
        A2: self.qp["Steve"] = 6. "Steve" is the 6th patient on the priority queue.
        Q3. Update the health score for "Joe" to 0?
        A3: (decreasing key) keys["Joe"] = 0, qp["Joe"] = 2 so _swim(2)
        Q4: Increase the health score for patient "Billy" to 6?
        A4: keys["Billy"] = 6, _sink(qp["Billy"]=2)
        

Indexed priority queues allow for:
1. Changing the prioirty of an index (vertex) in lg() time
2. Associating an index with each priority level 
3. The custom implementation allows indices to be any hashable object


"""
# Example:
# python indexed_priorityqueue_min_custom.py
import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_3.st_hashtable_separatechaining.st_hashtable_separatechaining import ST_HashTable_SeparateChaining

class Indexed_PriorityQueue_Min:
    def __init__(self):
        # 
        self.pq = []
        self.pq.append(None)
        
        self.keys = {}
        self.qp = {}
        self.node_count = 0
    
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
        
        self.pq.append(index)
        self.qp[index] = self.node_count+1
        
        self._swim(self.node_count+1)
        
        # self.qp is updated in the _swim() operation
        
        self.node_count +=1
    
    # Takes in an index value and returns True if the index is in the indexed_priority_queue
    def contains(self, index):
        return index in self.qp
    
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
        del self.keys[index]
        pqindex = self.qp[index]
        self.pq[pqindex] = self.pq[self.node_count]
        self.pq.pop()
        del self.qp[index]
        self.node_count -= 1
        self._sink(1)
    
    # Returns the smallest priority level / smallest key value
    def min(self):
        index = self.pq[1]
        key = self.keys[index]
        return key
    
    # Returns the smallest priority level / smallest key value
    # Deletes the smallest key value and its correspoding index (from self.keys, self.pq and self.qp)
    def delMin(self):
        index = self.pq[1]
        key = self.keys[index]
        
        # Delete this node by replacing it with node at end of priority queue
        self.pq[1] = self.pq[self.node_count]
        self.pq.pop()
        
        del self.qp[index]
        
        #self.node_count -= 1
        self.node_count -= 1
        self._sink(1)
        #self.node_count -= 1
        # Remove key
        del self.keys[index]
        return key


    
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
                least_child_node_key = self.keys[child_node_1_index]
        
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
    iPQ = Indexed_PriorityQueue_Min()

    iPQ.insert("Matt", 9)
    iPQ.insert("Bobby", 3)
    iPQ.insert("Joe", 6)
    iPQ.insert("Dil", 1)
    iPQ.insert("Pete", 5)
    iPQ.insert("Steve", 8)
    iPQ.insert("Dave", 4)
    iPQ.insert('Billy', 2)
    
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
    
    iPQ.delete("Dave")
    for i in iPQ:
        print(i)

    print(iPQ.contains("Joe"))
    print(iPQ.contains("Dave"))
    print(iPQ.min())
    
    
    iPQ.insert("Dave", 4)
    iPQ.insert("Dil", 1)
    
    iPQ.change("Joe", 0)
    print('\n')
    print(iPQ.keys)
    print(iPQ.pq)
    print(iPQ.qp)
    for i in iPQ:
        print(i) 
    

if __name__=="__main__": main()

               
        
        
    
    