# Title: stack_linkedlist.py
# Author: Ryan Borchardt

# I am implementing the stack data structure using an implementation of linked lists.
# I made the stack iterable.

# Example 1:
# python stack_linkedlist.py < tobe.txt

import sys

class Stack_LinkedList:
    def __init__(self):
        self._linked_list = None
        self._node_count = 0
        
        
    class _Node:
        def __init__(self, item):
            self.item = item
            self.next = None
            
    class _Iterator_Stack_LinkedList:
        def __init__(self, stack):
            self.current_node = stack._linked_list
        
        def __next__(self):
            if self.current_node == None: raise StopIteration
            returned_item = self.current_node.item
            self.current_node = self.current_node.next
            return returned_item
        
    def __len__(self):
        return self._node_count
    
    def isEmpty(self):
        return self._node_count==0
    
    def push(self, item):
        old_first_node = self._linked_list
        new_node = Stack_LinkedList._Node(item)
        new_node.next = old_first_node
        self._node_count += 1
        self._linked_list = new_node
    
    
    def pop(self):
        returned_item = self._linked_list.item
        self._linked_list = self._linked_list.next
        self._node_count -= 1
        return returned_item
    
    def __iter__(self):
        return Stack_LinkedList._Iterator_Stack_LinkedList(self)
    
    
def main():
    stack = Stack_LinkedList()
    print(len(stack))
    print(stack.isEmpty())
    
    stack.push('red')
    stack.push('green')
    stack.push('blue')
    stack.push('yellow')
    
    print(len(stack))
    print(stack.isEmpty())
    
    print(stack.pop())
    print(stack.pop())
    
    print(len(stack))
    
    stack.push('purple')
    stack.push('orange')
    stack.push('brown')
    
    for item in stack:
        print(item)
        
    print('-------')
        
    stack_2 = Stack_LinkedList()
    
    # sys.stdin.readlines() reads in (consumes) the entire contents of the file and returns a list of strings, where each string is a line from the file (separated by the newline character \n)
    # sys.stdin.readline() reads in (consumes) the first line of the file and returns it as a string.
    data = sys.stdin.readline()
    
    list_word_strings = data.split(" ")
    
    for word in list_word_strings:
        if word == "-":
            sys.stdout.write(str(stack_2.pop()) + " \n")
        else:
            stack_2.push(word)
    summary_string = "(" + str(len(stack_2)) + " left on stack)."
    sys.stdout.write(summary_string)
        
if __name__=="__main__": main()        
     
    
    
        