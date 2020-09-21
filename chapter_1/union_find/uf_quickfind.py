# Title: uf_quickfind.py
# Author: Ryan Borchardt

# The constructor involves s append() operations. append() is constant amortized time, so the order of growth of the constructor is s (linear).
# The union() method has a linear order of growth (s). 
# The find() method has a constant order of growth (1).
# The connected() method has a constant order of growth (1).
# The count() method has a constant order of growth (1).

# The test client main(): 
    # takes in the number of sites from random input (1, constant)
    # Runs the constructor for UF_basic (s, linear)
    # Runs the Union method() c times (s*c, quadratic)
    # Runs the count() method (1, constant)
    # Runs the connected method twice (1, constant).
    
    # Overall, the test client for UF_basic has a quadratic order of growth (s*c). 
    
    # tinyUF.txt has 10 sites (s=10) w/ 11 connections (c=11).
    # mediumUF.txt has 625 sites (s=625) w/ 900 connections (c=900)
    # largeUF.txt has 1 million sites (s=1 mil) w/ 2 million connections (c=2 mil)
    
    # python UF_basic.py < mediumUF.txt takes 0.0377 seconds (s*c=562,500)
    # Running the above instead with largeUF.txt would take ~ ((1 million* 2 million)/(562,500) * 0.0377 seconds = ~134,044 seconds = ~ 37 hours!) 

# Example:
# python UF_quickfind.py < tinyUF.txt
# python UF_quickfind.py < mediumUF.txt

import sys
import time

class UF_QuickFind:
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
    
    UF_structure = UF_QuickFind(num_sites)
    
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