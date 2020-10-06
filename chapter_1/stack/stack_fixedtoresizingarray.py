# Title: stack_fixedtoresizingarray.py
# Author: Ryan Borchardt

# This is a more advanced version of resizingarraystack.py. In this implementation, I am starting with using a fixed array (a numpy array in this case) rather than a resizing array (Python list). 
# I am including the functionality to specify the data type of the numpy array.
# I am also including the functionality to make stack_fixedtoresizingarray iterable.

# Example 1:
# python stack_fixedtoresizingarray.py tobe.txt " "

# Example 2:
# python stack_fixedtoresizingarray.py

import numpy as np
import sys

class Stack_FixedToResizingArray:
    def __init__(self, array_dtype):
        self.array_dtype = array_dtype
        self._a = np.empty(1, dtype=self.array_dtype)
        self.N = 0
        
    # Nested class
    class _Stack_FixedToResizingArray_Iterator:
        def __init__(self, stack):
            self._array = stack._a
            self._current_index = stack.N-1
        def __next__(self):
            if self._current_index == -1: raise StopIteration
            else:
                index_value = self._current_index
                self._current_index -= 1
                return self._array[index_value]
            
    
    def __len__(self):
        return self.N
    
    def isEmpty(self):
        return len(self)==0
        
    def resize(self, factor):
        intermediate = self._a
        self._a = np.empty(int(factor*len(self._a)), dtype=self.array_dtype)
        for i in range(self.N):
            self._a[i] = intermediate[i]
    
    def push(self, item):
        if self.N == self._a.size: self.resize(2)
            
        self._a[self.N] = item
        self.N +=1
        
    def pop(self):
        if self.N / self._a.size <= 0.25: self.resize(0.5) 
        self.N -=1
        popped_item = self._a[self.N]
        self._a[self.N] = None
        return popped_item
        
    def __iter__(self):
        # In python, to call on a nested class: outer_class.nexted_class()
        return Stack_FixedToResizingArray._Stack_FixedToResizingArray_Iterator(self)
        
def main():
    # If no filename is given:
    if len(sys.argv) == 1:
        ra_stack = Stack_FixedToResizingArray("object")

        ra_stack.push('red')
        ra_stack.push('blue')
        ra_stack.push('orange')
        ra_stack.push('purple')
        ra_stack.push('yellow')
        print(len(ra_stack))
        print(ra_stack.isEmpty())

        print(ra_stack.pop())

        print(len(ra_stack))


        # In its most basic form (just ResizingArrayStack(), len(), isEmpty(), push(), pop()) the object is not iterable.
        # The code below gives the following error: 'FixedToReszingArrayStack' object is not iterable.
        #for item in ra_stack:
        #    print(item)

        # In order to make an object iterable, the object must implement the special method __iter__() in support of the built-in function iter() whiches creates and returns an Iterator object.
        # The Iterator class must include the special method __next__(). The special method __next__() must return one element in the order that the data strucutre is defined to be iterated through.

        # the statement "for i in iterable_object" results in first, calling the iter() method on the iterable_object to return an iterator. It then calls the next() method on the iterator object. 
        # Each call on the next() method is one loop of the for loop. These loops continue until a StopIteration is raised. At this point, the for loop is completed.

        for item in ra_stack:
            print(item)

    # If a filename (the elements are restricted to being strings) is given:
    else:
        filename = sys.argv[1]
        delimiter = sys.argv[2]
        stack = Stack_FixedToResizingArray('object')
        # returns a file object
        data = open(filename, 'r')
        # returns a string of the first line of the file object
        first_line = data.readline()
        list_word_strings = first_line.split(delimiter)
    
        for word in list_word_strings:
            if word == "-":
                print(str(stack.pop()) + " \n")
            else:
                stack.push(word)
        summary_string = "(" + str(len(stack)) + " left on stack)."
        print(summary_string)
    
                            
        
if __name__=='__main__': main()