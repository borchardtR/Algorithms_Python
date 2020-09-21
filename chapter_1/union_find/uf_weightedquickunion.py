# Title: uf_weightedquickunion.py
# Author: Ryan Borchardt

# Weighted QuickUnion 

"""
The key to understanding the difference between quick_union and weighted_quick_union  
is understanding that the find() operation takes time (at most) proportional to the tree height (and at best constant). 

quick_union can have a tree height between 1 and s (# of sites).

weighted_quick_union can have a tree height between 1 and lg(s). 

The reason for this is that weighted_quick_union restricts the height of a tree to a max of lg(s) 
by when adding two trees together you assign the small tree to be connected to the larger tree (size of tree is determined by # of nodes/sites in the tree). 

Best case: 
By always connecting smaller tree to larger tree, the size of the tree increases while the height of the tree stays the same. 
See Proposition H on p.229 for the mathematical proof.

Worst case:
Both trees are the same size so choose one to connect to other. 
The size (# of nodes/sites) of the tree doubles while the height (max depth of the tree) increases by 1. 
This is logarithmic growth.
"""

# The constructor involves 2s append() operations. append() is constant amortized time, so the order of growth of the constructor is s (linear)
# The method count() takes constant time.
# The method find() depends on the input. 
#   It takes anywhere between constant time (best-case scenario where each site is its own root site / component) and 
#   logarithmic time (worst-case scenario where there is only one component and the site p is at the very bottom, the max depth of tree is lg(s) b/c the small tree is always added to larger tree). 
# The connected() method uses the find() method so it depends on the input. Best case is constant time, worst case logarithmic time.
# The union() method uses the find() method so it depends on the input as well. Best case is constant time, worst case logarithmic time.

# The test client main(): 
    # takes in the number of sites from random input (1, constant)
    # Runs the constructor for UF_basic (s, linear)
    # Runs the Union method() c times (beween c*1 and c*lg(s) so between linear time and linearithmic time)
    # Runs the count() method (1, constant)
    # Runs the connected method twice (between constant and logarithmic time).
    
    # Overall, the test client for quick union has an order of growth between linear and linearithmic, depending on the input. 
    
    # tinyUF.txt has 10 sites (s=10) w/ 11 connections (c=11).
    # mediumUF.txt has 625 sites (s=625) w/ 900 connections (c=900)
    # largeUF.txt has 1 million sites (s=1 mil) w/ 2 million connections (c=2 mil)     
    
    
    # This means that weighted quick union in the best case performs markedly better than quickfind (order of growths c vs c*s) and performs better in the worst case too(order of growths c*log(s) vs c*s).
    # Weighted quick union in the best case performs similar to quickunion in the best case: (c vs c) but weighted quick union performs better in the worse case ( c*log(s) vs c*s) 

# Example:
# python UF_weightedquickunion.py < tinyUF.txt       
    
 
import sys
import time
 
class UF_WeightedQuickUnion:
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
    
    UF_structure = UF_WeightedQuickUnion(num_sites)
    
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