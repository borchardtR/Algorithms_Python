"""
Title: uf_weightedquickunion_pathcompression.py
Author: Ryan Borchardt

Weighted QuickUnion with Path Compression


The key to understanding the difference between weighted quick union and weighted quick union with path compression  
is understanding that the find() operation includes an extra loop where for each site that was on the path, assign it to point towards the root of the tree (which is self.id[p] after the while loop terminates)

This extra for loop in the worst possible case keeps the time complexity of the find() operation to log(n) where n is the height of the tree.
Additional calls to find() (which is used by union() and connected()) that utilize a path with one of these sites is shortened.

"This helps to flatten the trees almost completely"

In the best case, the test client has time complexity of c O(1) operations.
In the worst case, the test client has time complexity of c O(close to 1) operations (approaches constant amortized time (but does not reach this ideal) (p.231). The proof of this is very complex.)
    
Example:
python UF_weightedquickunion_pathcompression.py < largeUF.txt       
"""    
 
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
        # Keeps track of all of the sites traversed to reach the root.
        path_list = []
        while p != self.id[p]: 
            #self.id[p] = id of the root which is self.id[p] on the final iteration
            path_list.append(p)
            p=self.id[p]
        # For each site that was on the path, assign it to point towards the root of the tree (which is self.id[p] after the while loop terminates)
        for site in path_list:
            self.id[site] = self.id[p]
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