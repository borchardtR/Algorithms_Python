# Title: stack_resizingarray.py
# Author: Ryan Borchardt

# Writing Stack_ResizingArray in Python after seeing its implementation in Java. In this implementation, I am starting with using a resizing/dynamic array (Python lists). 
# Note that I am including the functionality to make Stack_ResizingArray iterable.
# I included two different test clients. One that uses python's built in open function () and another that uses standard input.


# Comments:

# An array must support the following operations:
# 1. Creation
# 2. Indexed access
# 3. Indexed assignment
# 4. Iteration (note that an array in Java is not iterable)


# Python lists are an advanced form of an array because:
# 1. Python lists are dynamic/resizing arrays (Java arrays are fixed in size).
# 2. Python lists can hold references to any data type (Java requires the use of generics to achieve this functionality)
# 3. Python lists can hold references to multiple different data types (Java can't do this).
# 4. Python lists are iterable (You can iterate through a Java array but not inherently -> You would have to do something like: for (int i = 0; i < N; i++) a[i] = a[i]+1. In Python lists you can do something like this: for item in a: print(item)


# Collections are characterized by five operations:
# 1. Create the collection
# 2. Insert an item
# 3. Remove an item
# 4. Test whether the collection is empty
# 5. Determine its size/number of items

# A sequence is an iterable object that has an index from 0 to n-1. Lists, tuples, ranges are sequences. Dictionaries, sets etc are not. Dictionaries and sets are still iterables, however b/c they contain an iter() method that returns an iterator object. The iterator object contains a next method that returns each item in the iterable object. 


# I decided to make Stack_ResizingArray iterable

# Sources
# 1. Pages 661-662 of Sedgewick's Python
# 2. Pages 138-139 of Sedgewick's Algorithms
# 3. https://www.novixys.com/blog/nested-inner-classes-python/ 
# 4. https://treyhunner.com/2016/12/python-iterator-protocol-how-for-loops-work/ 
# 5. https://towardsdatascience.com/python-basics-iteration-and-looping-6ca63b30835c 
# 6. https://realpython.com/python-for-loop/


# When you use a for loop, what is happening under the hood is: the iter() method is called on the iterable object in the 'for item in iterable_object' statement
# The iter() method returns an iterator object. This iterator object is used to iterate through each of the items in the iterable object. It contains the next() method, which returns an item.
# The next() method is called repeatedly on the iterator object until the raise StopIteration occurs. At this point, the for loop has finished.


# Example 1:
# python stack_resizingarray.py tobe.txt " "

# Example 2:
# python stack_resizingarray.py

import sys

class Stack_ResizingArray:
    def __init__(self):
        self._a = []
    
    # nested class. The leading underscore is used to indicate that this class should be private (not enforced in Python).    
    class _Stack_ResizingArray_Iterator:
        def __init__(self, ra_stack_object):
            self.current_index = len(ra_stack_object)
            self.array = ra_stack_object._a
            
        def __next__(self):
            if self.current_index <= 0:
                raise StopIteration
            self.current_index -= 1
            return self.array[self.current_index]
        
    def isEmpty(self):
        return len(self._a) == 0
        
    def __len__(self):
        return len(self._a)
        
    def push(self, item):
        self._a += [item]
        
    def pop(self):
        return self._a.pop()
        
        
    # In order to make an object iterable, the object must implement the special method __iter__() in support of the built-in function iter() whiches creates and returns an iterator object.
    # The iterator class must include the special method __next__() which returns the next item in the iterable
    
    def __iter__(self):
        return Stack_ResizingArray._Stack_ResizingArray_Iterator(self)
        
# Test client 

#Method 1: the built-in open() function  
#def main():
    
    # f is a file object.
    # file objects are iterable
    # a file object consists of a sequence of string objects (each line in the file is a string object). Each line is separated by the \n newline character.
    # requires specific file name in code so not as flexible 
    #stack = Stack_ResizingArray()
   
   #f = open('tobe.txt', 'r')

    #first_line_string = f.readline()
    #f.close()
    #list_word_strings = first_line_string.split(" ")
    
    #for word in list_word_strings:
    #    if word == "-":
    #        print(stack.pop())
    #    else:
    #        stack.push(word)
    # In Python, the concatenation operator doesn't automatically convert int to str.
    #summary_string = "(" + str(len(stack)) + " left on stack)."
    #print(summary_string)
    
    #Alternative: In Python, the built-in print() function does convert int to str.
    #print("(",len(stack),"left on stack).")
    
    
# Method 2: using the stdin module from the sys library
# Allows flexibility of specifying any file.
# Uses the following format: python stack_resizingarray.py < tobe.txt

def main():
    # If no filename is given:
    if len(sys.argv) == 1:
        ra_stack = Stack_ResizingArray()

        ra_stack.push('red')
        ra_stack.push('blue')
        ra_stack.push('orange')
        ra_stack.push('purple')
        ra_stack.push('yellow')
        print(len(ra_stack))
        print(ra_stack.isEmpty())

        print(ra_stack.pop())

        print(len(ra_stack))


        # In its most basic form (just Stack_ResizingArray(), len(), isEmpty(), push(), pop()) the object is not iterable.
        # The code below gives the following error: 'FixedToReszingArrayStack' object is not iterable.
        #for item in ra_stack:
        #    print(item)

        # In order to make an object iterable, the object must implement the special method __iter__() in support of the built-in function iter() whiches creates and returns an Iterator object.
        # The Iterator class must include the special method __next__(). The special method __next__() must return one element in the order that the data strucutre is defined to be iterated through.

        # the statement "for i in iterable_object" results in first, calling the iter() method on the iterable_object to return an iterator. It then calls the next() method on the iterator object. 
        # Each call on the next() method is one loop of the for loop. These loops continue until a StopIteration is raised. At this point, the for loop is completed.

        for item in ra_stack:
            print(item)

    # If a filename is given:
    else:
        filename = sys.argv[1]
        delimiter = sys.argv[2]
        stack = Stack_ResizingArray()
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