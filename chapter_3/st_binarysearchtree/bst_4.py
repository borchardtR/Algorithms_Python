# bst_2.py is the traditional way of implementing a BST.
    # The put() (and _put()) operation does NOT return a node going back up the call stack. 
        # It just keeps calling until it finds the node where node.key == key or where the node is None.
        # When the _put() method is called for a given node, we know ahead of time that that node is NOT None.
        # This makes determining the size of each node (which is necessary for select() and rank() operations) much less efficient (would have to use lazy method).
            # Before using the select and rank operations, you could perform a size operation that takes linear time by going through each node and updating the size of each node.
                # Could use some sort of caching if the bst.node_count == self.root.size, you don't have to perform the size operation
                # Even with caching, this could result in a really inefficent method if rank() and select() are called frequently and/or interspersed with put() and delete() operations!           
    # When the _get() method is called for a given node, we know ahead of time that the node is NOT None.

# bst_3.py is the way Sedgewick implements a BST.
    # The put() (and _put()) operation returns a node going back up the call stack.
        # This allows us to easily modify the size parameter of each node going back up the call stack (the eager method takes time proportional to the length of the path).
        # When the _put() method is called for a given node, we do NOT know ahead of time if the node is None.
        # When the _get() method is called for a given node, we do NOT know ahead of time that the node is not None.
        # This method has more carry-over to more complicated BST structures like the red-black tree.

# python bst_4.py

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.size = 1
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.nodes = 0
    
    def put(self, key, value):
        self.root = self._put(self.root, key, value)
            
    
    def _put(self, node, key, value):
        if node== None:
            return Node(key, value)
        
        elif key==node.key:
            node.value = value
            return node
        
        elif key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        return node
        
    def get(self, key):
        return self._get(self.root, key)
    
    def _get(self, node, key):
        if node == None:
            return None
        if key==node.key:
            return node.value
        elif key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key) 
            
    def minimum(self):
        if self.root == None:
            return None
        else:
            return self._minimum(self.root)
    
    def _minimum(self, node):
        if node.left == None:
            return node.key
        else:
            return self._minimum(node.left)
    
    def floor(self, key):
        
    
        
def main():
    bst = BST()
    bst.put('Jim', 22)
    bst.put('Frank', 54)
    bst.put('Billy', 36)
    bst.put('Hank', 87)
    bst.put('Tom', 18)
    bst.put('Xavier', 44)
    bst.put('Ernie', 112)
    bst.put('Sam', 47)
    
    print(bst.get('Hank'))
    print(bst.minimum())
    
if __name__=="__main__": main()
        
        
        
        