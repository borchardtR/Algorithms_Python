# Title: 256way_trie.py
# Author: Ryan Borchardt

# This is a specific implementation of an R-way trie. My particular implementation is restricted to being a 256-way trie b/c I rely on the built-in Python ASCII functions ord() and chr() 
# See rway_trie.py for an implementation of a true R-way tree. 
# Implements the API on page 730.

# Time complexities:
# Search hit time complexity: ~length(key) (in all cases) 
# Insert time complexity: ~length(key) (in all cases)
# Search miss time complexity: ~0 (in the best case), ~length(key) (in the worst-case), and ~log(N,R) in the average case (where N is the # of keys and R is the length of the alphabet).

# Space complexities:
# R*N in the best-case (almost complete overlap of keys over nodes)
# R*N*w in the worst-case (almost not overlap of keys over nodes) where w is average key length.


# Example:
# python 256way_trie.py seashore.txt ' '


import sys
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList

class Node:
    def __init__(self, R):
        self.links = [None]*R
        self.value = None
        
class Trie:
    def __init__(self):
        self.R = 256
        self.root = None
        self.root_size = 0
       
    def put(self, key, value):
        self.root = self._put(self.root, 0, key, value)
        
    def _put(self, current_node, d, key, value):
        if current_node == None:
            current_node = Node(self.R)
        
        if d == len(key):
            # If this node didn't already have a value (ie we aren't replacing a value for an existing key) increment _size by 1
            if current_node.value == None:
                self.root_size += 1
            current_node.value = value
            return current_node
        index = ord(key[d])
        d+= 1
        current_node.links[index] = self._put(current_node.links[index],d,key,value)
        #if final node didn't already have a value:
        #current_node._size += 1
        return current_node
        
    def get(self, key):
        node_with_key = self._get(self.root, 0, key)
        if node_with_key == None:
            return None
        return node_with_key.value
        
        
    def _get(self, current_node, d, key):
        if current_node == None:
            return None
        if d == len(key):
            return current_node
        index = ord(key[d])
        d += 1
        return self._get(current_node.links[index], d, key)
        
    def contains(self, key):
        return self.get(key) != None
        
    def isEmpty(self):
        return self.root_size != 0
    
    def size(self):
        return self.root_size
    
    # Returns a queue of the keys, which is an iterable object
    def keys(self):
        queue = Queue_LinkedList()
        self.collect(node=self.root, pre="", queue=queue)
        return queue
    
    # Returns a queue of the keys with the specified prefix, which is an iterable object
    def keysWithPrefix(self, pre):
        node = self._get(self.root,0,pre)
        queue = Queue_LinkedList()
        self.collect(node=node, pre=pre, queue=queue)
        return queue
        
    def collect(self, node, pre, queue):
        if node==None:
            return
        if node.value != None:
            queue.enqueue(pre)
            
        for i in range(0,len(node.links)):
            char = chr(i)
            self.collect(node.links[i], pre+char, queue)
    
    # wildcard matching
    def keysThatMatch(self, pat):
        queue = Queue_LinkedList()
        self.wildcard_collect(node = self.root, pre="", pat=pat, queue=queue)
        return queue
    
    def wildcard_collect(self, node, pre, pat, queue):
        d = len(pre)
        if node == None:
            return
        # Compared to the two previous methods (keys() and keyswithPrefix(), keys only get added if they match the same length as pat.
        if d == len(pat) and node.value != None:
            queue.enqueue(pre)
        if d == len(pat): # and node.value == None
            return
        
        char = pat[d] 
        for i in range(len(node.links)):
            # if char is the wildcard character, search every reference in links (b/c any character is valid for the wildcard character)
            # or if char is a letter, search that link
            if char=='.' or ord(char)==i:
                self.wildcard_collect(node.links[i], pre=pre+chr(i), pat=pat, queue=queue)
    
    def longestPrefixOf(self, string):
        length =  self.search(self.root, string, 0, 0)
        return string[0:length]
        
    def search(self, node, s, d, length):
        if node == None:
            print(length)
            return length
        
        # If you encounter a key, update the length.
        if node.value != None:
            length = d
        
        # The longest the length can possibly be is the length of the string:
        if d==len(s):
            return length
            
        char = s[d]
        
        node = node.links[ord(char)]
        d += 1
        
        return self.search(node, s, d, length)
    
    def delete(self, key):
        self._delete(self.root, key, 0)
        
    def _delete(self, node, key, d):
        
        if d == len(key) and node.value != None:
            node.value = None
            print('deleted key')
            return
            
        if d == len(key) and node.value == None:
            print('Key does not exist')
            return 
            
        char = key[d]
        next_node = node.links[ord(char)]
        d += 1
        
        self._delete(next_node, key, d)
        
        for i in range(len(next_node.links)):
            downstream_node = next_node.links[i]
            if downstream_node != None:
                # Cant delete node because there are other keys that use these downstream nodes
                return
        
        # If no downstream keys, delete reference to node:
        node.links[ord(char)] = None
        self.root_size -= 1
    
def main():
    
    trie = Trie()
    
    file_object = open(sys.argv[1], 'r')
    output_list = file_object.readlines()
    word_count =0
    
    for line in output_list:
        list_strings = line.split(sys.argv[2])
        for word in list_strings:
            print("put operations:")
            print(word, word_count)
            trie.put(word, word_count)
            word_count += 1        
    
    print('sea', trie.get('sea'))   
    print('shells', trie.get('shells'))
    print('shortes', trie.get('shortes'))
    
    print(trie.contains('sea'))
    
    print(trie.isEmpty())
    print(trie.size())
    
    print("Keys in the trie:")
    for i in trie.keys():
        print(i)
    
    print("\n\n")
    print("Keys with the prefix 'sh':")
    for i in trie.keysWithPrefix("sh"):
        print(i)
    
    print("Keys that match 'sh.':")
    for i in trie.keysThatMatch('sh.'):
        print(i)
    
    print("Longest prefix of 'shellsort':")
    print(trie.longestPrefixOf("shellsort"))
    
    trie.delete('by')
    
    trie.delete('sea')
    
    trie.delete('she')
    
    print(trie.get('by'))
    print(trie.get('sells'))
    print(trie.get('shore'))
    
    print(trie.size())
    
if __name__=="__main__": main()