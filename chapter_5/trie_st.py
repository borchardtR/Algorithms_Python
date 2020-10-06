# Title: trie_st.py
# Author: Ryan Borchardt

# Example:
# python trie_st.py seashore.txt ' '


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')
from algorithms_python.chapter_4.edge_weighted_digraphs.edge_weighted_digraph import Edge_Weighted_Digraph
from algorithms_python.chapter_1.stack.stack_resizingarray import Stack_ResizingArray

class Node:
    def __init__(self, R):
        self.value = None
        self.links = [None]*R

class Trie_ST:
    def __init__(self):
        self.R = 256
        self.root = None
        self.root_size = 0
    
    def put(self, key, value):
        self.root = self._put(self.root, key, 0, value)
        
    
    def _put(self, node, key, d, value):
        if node == None:
            node = Node(self.R)
        if d == len(key)-1:
            if node.value == None:
                self.root_size += 1
            node.value = value
            return node
        letter = key[d]
        index_num = ord(letter)
        node.links[index_num] = self._put(node.links[index_num], key, d+1, value)
        return node
    
    def get(self, key):
        node = self.root
        d = 0
        return self._get(node, key, d)
        
    def _get(self, node, key, d):
        if node == None:
            return None
        elif d == len(key)-1:
            return node.value
            
        character = key[d]
        character_index = ord(character)
        return self._get(node.links[character_index], key, d+1)
    
    def contains(self,key):
        return self.get(key) != None
    
    def isEmpty(self):
        return self.root_size != 0
    
    def size(self):
        return self.root_size
        
        
    def delete(self, key):
        if self.get(key) == None:
            raise Exception('Key is not in trie')
        node = self.root
        d = 0
        self.root = self._delete(node, key, d)
        
    def _delete(self, node, key, d):
        if d == len(d)-1:
            node.value == None
            return
        character_index = ord(key[d])
        next_node = node.links[character_index]
        node = self._delete(next_node, key, d+1)
        for i in range(len(node.links)):
            if (node.links[i])!= None
                return node
        return None
        

def main():
    
    trie = Trie_ST()
    
    file_object = open(sys.argv[1], 'r')
    output_list = file_object.readlines()
    word_count =0
    
    for line in output_list:
        list_strings = line.split(sys.argv[2])
        for word in list_strings:
            trie.put(word, word_count)
            word_count += 1        
        
    print(trie.get('shells'))
    print(trie.get('shortes'))
    
    print(trie.contains('sea'))
    
    print(trie.isEmpty())
    print(trie.size())
    

    
if __name__=="__main__": main()