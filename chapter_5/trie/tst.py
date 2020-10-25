# Title: tst.py
# Author: Ryan Borchardt

# This is an implementation of a ternary search trie.


# Implements the API on page 730.
# Have not implemented the keysThatMatch(), longestPrefixOf() or delete() methods for this data structure.

# Time complexities:
# Search hit time complexity: ~length(key) -> ~R*length(key)
# Insert time complexity: ~length(key) -> ~R*length(key)
# Search miss time complexity: ~1 (in the best case), ~R*length(key) (in the worst-case), and ~ln(N) in the average case (where N is the # of keys).

# Space complexities:
# 3*N in the best-case (almost complete overlap of keys over nodes)
# 3*N*w in the worst-case (almost not overlap of keys over nodes) where w is average key length.

# Example:
# python tst.py seashore.txt ' ' 


import sys
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_1.queue.queue_linkedlist import Queue_LinkedList
from algorithms_python.chapter_3.st_hashtable_separatechaining.st_hashtable_separatechaining import ST_HashTable_SeparateChaining

class Node:
    def __init__(self, character):
        self.character = character
        self.value = None
        
        self.less = None
        self.middle = None
        self.greater = None
        
        
class Trie:
    def __init__(self):
        self.root = None
        self.root_size = 0
    
    def put(self, key, value):
        self.root = self._put(self.root, 0, key, value)
        
    def _put(self, current_node, d, key, value):
        if current_node is None:
            current_node = Node(character=key[d])
        
        if d == len(key)-1 and key[d] == current_node.character:
            # If this node didn't already have a value (ie we aren't replacing a value for an existing key) increment _size by 1
            if current_node.value is None:
                self.root_size += 1
            current_node.value = value
            return current_node
        
        if key[d] < current_node.character:
            current_node.less = self._put(current_node.less, d, key, value)
        # only increment d in this case:
        elif key[d] == current_node.character:
            d += 1
            current_node.middle = self._put(current_node.middle, d, key, value)        
        elif key[d] > current_node.character:
            current_node.greater = self._put(current_node.greater, d, key, value) 
        
        return current_node
        
    def get(self, key):
        node_with_key = self._get(self.root, 0, key)
        if node_with_key is None:
            return None
        return node_with_key.value
        
        
    def _get(self, current_node, d, key):
        if current_node is None:
            return None
        if d == len(key)-1 and key[d] == current_node.character:
            return current_node
        
        if key[d] < current_node.character:
            return self._get(current_node.less, d, key)
        # only increment in this case (successfully traversed through node containing a character in the key)
        elif key[d] == current_node.character:
            d += 1
            return self._get(current_node.middle, d, key)        
        elif key[d] > current_node.character:
            return self._get(current_node.greater, d, key) 
     
       
        
    def contains(self, key):
        return self.get(key) is not None
        
    def isEmpty(self):
        return self.root_size == 0
    
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
        self.collect(node=node.middle, pre=pre, queue=queue)
        return queue
        
    def collect(self, node, pre, queue):
        if node is None:
            return
        if node.value is not None:
            print(pre+node.character)
            queue.enqueue(pre+node.character)
        
        self.collect(node.less, pre, queue)
        self.collect(node.middle, pre+node.character, queue)
        self.collect(node.greater, pre, queue)
    
    # wildcard matching
    #def keysThatMatch(self, pat):
    #    queue = Queue_LinkedList()
    #    self.wildcard_collect(node = self.root, pre="", pat=pat, queue=queue)
    #    return queue
    
    #def wildcard_collect(self, node, pre, pat, queue):
    #    d = len(pre)
    #    if node.character != pat:
    #        return
        # Compared to the two previous methods (keys() and keyswithPrefix(), keys only get added if they match the same length as pat.
    #    if d == len(pat) and node.value != None:
    #        print(pre)
    #        queue.enqueue(pre)
    #    if d == len(pat): # and node.value == None
    #        return
        
    #    char = pat[d]
    #    if char=='.':
    #        self.wildcard_collect(node.middle, pre=pre+node.middle.character, pat=pat, queue=queue)
    #    else:
    #        self.wildcard_collect(node.middle, pre=pre+char, pat=pat, queue=queue)
        
    
    #def longestPrefixOf(self, string):
    #    length =  self.search(self.root, string, 0, 0)
    #    return string[0:length]
        
    #def search(self, node, s, d, length):
    #    if node == None:
    #        print(length)
    #        return length
        
        # If you encounter a key, update the length.
    #    if node.value != None:
    #        length = d
        
        # The longest the length can possibly be is the length of the string:
    #    if d==len(s):
    #        return length
            
    #    char = s[d]
        
    #    node = node.links[self.toIndex(char)]
    #    d += 1
        
    #    return self.search(node, s, d, length)
    
    def delete(self, key):
        self._delete(self.root, key, 0)
        
    def _delete(self, node, key, d):
        
        if d == len(key) and node.value is not None:
            node.value = None
            print('deleted key')
            return
            
        if d == len(key) and node.value is None:
            print('Key does not exist')
            return 
            
        char = key[d]
        next_node = node.links[self.toIndex(char)]
        d += 1
        
        self._delete(next_node, key, d)
        
        for i in range(len(next_node.links)):
            downstream_node = next_node.links[i]
            if downstream_node is not None:
                # Cant delete node because there are other keys that use these downstream nodes
                return
        
        # If no downstream keys, delete reference to node:
        node.links[self.toIndex(char)] = None
        self.root_size -= 1
    
def main():
    
    trie = Trie()
    
    file_object = open(sys.argv[1], 'r')
    output_list = file_object.readlines()
    file_object.close()
    word_count =0
    
    for line in output_list:
        list_strings = line.split(sys.argv[2])
        for word in list_strings:
            print("put operations:")
            print(word, word_count)
            trie.put(word, word_count)
            word_count += 1        
    
    
    print('\n\n')
    
    
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
    
    #print("Longest prefix of 'shellsort':")
    #print(trie.longestPrefixOf("shellsort"))
    
    #trie.delete('by')
    
    #trie.delete('sea')
    
    #trie.delete('she')
    
    #print(trie.get('by'))
    #print(trie.get('sells'))
    #print(trie.get('shore'))
    
    #print(trie.size())
    
if __name__=="__main__": main()