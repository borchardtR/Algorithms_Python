# Title: uf_weightedquickunion.py
# Author: Ryan Borchardt

# Weighted QuickUnion 

# The constructor involves n append() operations. append() is constant amortized time, so the order of growth of the constructor is n (linear)
# The method count() takes constant time.
# The method find() depends on the input. 
#   It takes anywhere between constant time (best-case scenario where each site is its own root site / component) and 
#   logarithmic time (worst-case scenario where there is only one component and the site p is at the very bottom, the max depth of tree is lg(N) b/c the small tree is always added to larger tree). 
# The connected() method uses the find() method so it depends on the input. Best case is constant time, worst case logarithmic time.
# The union() method uses the find() method so it depends on the input as well. Best case is constant time, worst case logarithmic time.

# The test client main(): 
    # takes in the number of sites from random input (1, constant)
    # Runs the constructor for UF_basic (n, linear)
    # Runs the Union method() n times (beween n*1 and n*lg(N) so between linear time and linearithmic time)
    # Runs the count() method (1, constant)
    # Runs the connected method twice (between constant and linear time).
    
    # Overall, the test client for quick union has an order of growth between linear and linearithmic, depending on the input. 
    
    # This means that weighted quick union in the best case performs markedly better than quickfind (order of growths n vs n^2) and performs better in the worst case too(order of growths nlog(n) vs n^2).
  
# Example:
# python UF_weightedquickunion.py < tinyUF.txt       
    
 
import sys
import time
 
class uf_weightedquickunion:
    def __init__(self, num_sites):
        self.component_count = num_sites
        self.id = []
        self.tree_size = []
        for i in range(num_sites):
            self.id.append(i)
            self.tree_size.append(1)
    
    # Add connection between site p and site q (side-effect, no return value)
    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        
        if p_root == q_root: return
        else:
            # Assign smaller sized tree to larger sized tree
            
            # If the tree size for p_root is smaller than the tree size for q_root, assign the p_root tree to q_root.
            if self.tree_size[p_root] < self.tree_size[q_root]: 
                self.id[p_root] = q_root
                # Determine the new tree size. Only need to keep track of the tree size at the root of the tree (in this case q_root) b/c only the root of a tree is ever called upon in union. 
                # The tree size for p_root doesn't need to be updated b/c it is no longer a root.
                self.tree_size[q_root] += self.tree_size[p_root]
            # If the tree size for q_root is smaller than the tree size for p_root, assign the q_root tree to p_root.
            else:
                self.id[q_root] = p_root
                # Determine the new tree size. Only need to keep track of the tree size at the root of the tree (in this case p_root) b/c only the root of a tree is ever called upon in union. 
                # The tree size for q_root (and any other size that is part of the tree) doesn't need to be updated b/c it is no longer a root.        
                self.tree_size[p_root] += self.tree_size[q_root]
    
    # Find and return the root site for site p (ie find component number for site p)
    def find(self, p):
        while p != self.id[p]: p=self.id[p]
        return self.id[p]
    
    # Return true if site p and site q are from the same component, false if not
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    # Return the number of components
    def count(self):
        return self.component_count
    
    
def main():
    start = time.time()
    # Test client to take in sequence of integers file from standard input
    num_sites = int(sys.stdin.readline())
    
    UF_structure = uf_weightedquickunion(num_sites)
    
    for line in sys.stdin:
        pair_list = line.split(" ")
        p = int(pair_list[0])
        q = int(pair_list[1])
        UF_structure.union(p,q)
        
    print(UF_structure.count())
    
    #for i in range(num_sites):
    #    print(UF_structure.find(i))

    print(UF_structure.connected(3,7))
    print(UF_structure.connected(3,8))
    
    finish = time.time()
    
    print(finish-start)

if __name__=="__main__": main()