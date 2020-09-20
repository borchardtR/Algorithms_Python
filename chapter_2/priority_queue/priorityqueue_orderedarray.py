# Title: priorityqueue_orderedarray.py
# Author: Ryan Borchardt

# I am implementing the priority queue data structure using a resizing array (python list).
# I am intentionlly NOT using the python list method insert() b/c I wanted to go through the challenge/exercise of doing it myself. 
# I made the priority queue iterable.


# The insert() method takes linear time.
# The delMax() method takes constant time.

# Example:
# python priorityqueue_orderedarray.py


class PriorityQueue_OrderedArray:

    class _Iterator:
        def __init__(self, PQ_object):
            self.array = PQ_object._a
            self.current_index = PQ_object.size()-1
        def __next__(self):
            if self.current_index <0: raise StopIteration
            returned_item = self.array[self.current_index]
            self.current_index -= 1
            return returned_item
            
    
    def __init__(self):
        self._a = []
    
    # Constant time
    def isEmpty(self):
        return len(self._a) == 0
    # Constant time    
    def size(self):
        return len(self._a)

    # Linear time    
    # First: find where inserted item should be inserted into ordered array (constant-linear time)
    # Second: move all entries larger than inserted item to the right (constant-linear time)
    # These two operations take inverse time to eachother (if the first operation is short, the second operation is long and vice-versa)
    
    def insert(self, v):
        # Python's built-in resizing array (list) structure is iterable
        
        if self.isEmpty():
            self._a.append(v)
            return
        
        # 1. Find where the inserted item should be inserted into ordered array:
        item_index=0
        at_end=True
        for item in self._a:
            if v <= item:
                inserted_item_index = item_index
                at_end=False
                break
            item_index += 1
        # If v is the max value, append it to the end and return.
        if at_end==True:
            self._a.append(v)
            return
        
        # 2. Insert v into the correct item index:
        # Note that I am choosing not to use the built in method insert() for lists b/c I wanted the challenge/exercise of doing it myself
        temp1 = self._a[inserted_item_index]
        self._a[inserted_item_index] = v
        
        # 3. Shift all entries to the right of the inserted item down 1:
        for i in range(inserted_item_index+1,self.size()):
            temp2 = self._a[i]
            self._a[i] = temp1
            temp1=temp2
        # This last value is added b/c the new array is 1 entry longer than before the insertion
        self._a.append(temp1)
            
        
    # Constant time
    def max(self): 
        return self._a[self.size()-1]
    
    # Constant time        
    def delMax(self):
        return self._a.pop()
        
    def __iter__(self):
        return PriorityQueue_OrderedArray._Iterator(self)
        
def main():

    PQ = PriorityQueue_OrderedArray()
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