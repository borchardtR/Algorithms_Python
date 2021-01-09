# Title: PQ_max.py
# Author: Ryan Borchardt

# I am implementing the priority queue data structure using a binary heap.
# I am implementing the binary heap data structure using an array (Python list). The binary-heap is 1-indexed (the first node is at a[1]) with a[0] being unused.
# I made the priority queue iterable.

# Example:
# python PQ_max.py

class PQ_Max:

    def __init__(self):
        self.heap = [0]
        self.count = 0
        
    def insert(self,v):
        self.count+=1
        self.heap.append(v)
        self._swim(self.count)
    
    def max(self):
        return self.heap[1]
    
    def delMax(self):
        maximum = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.count-=1
        self._sink(1)
        return maximum
    
    def isEmpty(self):
        return self.count==0
    
    def size(self):
        return self.count
    
    def _swim(self, node_index):
        parent_index = node_index//2
        
        while node_index>1 and self.heap[parent_index] < self.heap[node_index]:
            temp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[node_index]
            self.heap[node_index] = temp
            
            node_index = parent_index
            parent_index = node_index//2
    
    def _sink(self, node_index):
        
        while 2*node_index <= self.count:
            child_1_index = node_index*2
            child_2_index = node_index*2+1
            larger_child_index = child_1_index
            if child_2_index <= self.count:
                if self.heap[child_2_index] > self.heap[child_1_index]:
                    larger_child_index = child_2_index
            
            if self.heap[node_index] > self.heap[larger_child_index]:
                break
            
            temp = self.heap[larger_child_index]
            self.heap[larger_child_index]= self.heap[node_index]
            self.heap[node_index] = temp
            
            node_index = larger_child_index
            
    def __iter__(self):
        return PQ_Max._Iterator(self)
        
    class _Iterator:
        def __init__(self, max_pq):
            self.heap = max_pq.heap
            self.current = 1
            self.max_count = max_pq.count
        
        def __next__(self):
            if self.current > self.max_count: raise StopIteration
            returned = self.heap[self.current]
            self.current+=1
            return returned
            

            
def main():
    PQ = PQ_Max()
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
