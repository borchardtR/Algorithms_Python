# Title: priorityqueue_unorderedarray.py
# Author: Ryan Borchardt

# I am implementing the priority queue data structure using a resizing array (python list) that I structure to be unordered.
# I made the priority queue iterable.
# I am doing this on my own as an exercise.

# Example:
# python priorityqueue_unorderedarray.py

class PriorityQueue_UnorderedArray:
    def __init__(self):
        self._a = []
        
    class _Iterator:
        def __init__(self, PQ_object):
            self._array = PQ_object._a
            self.current_index = 0
            
        def __next__(self):
            if self.current_index >= len(self._array): raise StopIteration
            returned_item = self._array[self.current_index]
            self.current_index += 1
            return returned_item
            
    
    # Constant time    
    def size(self):
        return len(self._a)
    
    # Constant time        
    def isEmpty(self):
        return self.size()==0
    
    # Constant time        
    def insert(self, v):
        self._a.append(v)
    
    # Linear time    
    def max(self):
        max_element = self._a[0]
        for element in self._a:
            if element > max_element:
                max_element = element
                
        return max_element
        
    # Linear time 
    # 1. Find maximum element 
    # 2. Delete this element and shift all elements to the right of it over 1 to the left
    def delMax(self):
        max_index = 0
        max_element = self._a[0]
        for i in range(1,self.size()):
            if self._a[i] > max_element:
                max_element = self._a[i]
                max_index = i
        
        for i in range(max_index+1,self.size()):
            self._a[i-1] = self._a[i]
        self._a.pop()
        return max_element
    # In order for an object to be iterable, it must implement the iter() function which must return an Iterator
    # The Iterator must have a next() method which, each time it is called, returns the next element in the structure. The next method is called repeatedly until the StopIteration commmand is raised (implementation must define when this should occur)        
    
    def __iter__(self):
        return PriorityQueue_UnorderedArray._Iterator(self)
       
    
        
        
def main():
    PQ = PriorityQueue_UnorderedArray()
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