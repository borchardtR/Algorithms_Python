# Title: uf_basic.py
# Author: Ryan Borchardt

# This is my personal own initial implementation of UnionFind. 
# The constructor involves n append() operations. append() is constant amortized time, so the order of growth of the constructor is n (linear).
# The union() method has a linear order of growth (n). 
# The find() method has a constant order of growth (1).
# The connected() method has a constant order of growth (1).
# The count() method has a constant order of growth (1).

# The test client main(): 
    # takes in the number of sites from random input (1, constant)
    # Runs the constructor for uf_basic (n, linear)
    # Runs the Union method() n times (n^2, quadratic)
    # Runs the count() method (1, constant)
    # Runs the connected method twice (1, constant).
    
    # Overall, the test client for uf_basic has a quadratic order of growth (n^2). 
    
    
    # python uf_basic.py < mediumUF.txt takes 0.0377 seconds (n=625)
    # Running the above instead with largeUF.txt would take ~ ((1,000,000^2)/(625) * 0.0377 seconds = 2560000 seconds = ~ 27 hours!) 

# Example:
# python uf_basic.py < tinyUF.txt

import sys
import time

class uf_basic:
    def __init__(self, num_sites):
        self.component_count = num_sites
        self.id = []
        for i in range(num_sites):
            self.id.append(i)
    
    # Add connection between site p and site q (side-effect, no return value)
    def union(self, p, q):
        if self.id[p] != self.id[q]:
            old_q_component = self.id[q]
            self.id[q] = self.id[p]
        
            # Then need to update any sites belonging to q's old component to p's component.
            for i in range(len(self.id)):
                if self.id[i] == old_q_component: self.id[i] = self.id[p]
            
            self.component_count -= 1
        
    
    # Find and return the component number for site p    
    def find(self, p):
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
    
    UF_structure = uf_basic(num_sites)
    
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