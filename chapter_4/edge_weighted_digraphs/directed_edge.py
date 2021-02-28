# Title: directed_edge.py
# Author: Ryan Borchardt


# Example:
# python directed_edge.py 4 5 0.35


import sys

class Directed_Edge:
    def __init__(self, v, w, weight):
        self._from_vert = v
        self._towards_vert = w
        self._weight = weight
    
    def weight(self):
        return self._weight
    
    #from is a Python keyword.
    # It is bad practice to use keywords as a variable name, function name, instance method name etc so I use from_vert() instead.
    def from_vert(self):
        return self._from_vert
    
    def towards_vert(self):
        return self._towards_vert
    
    # Instead of compareTo(), I will be using the 6 special instance methods that establish an Edge object as comparable and define a total order
    # The _weight instance variable is a float object. float objects are comparable.
    def __eq__(self,other):
            return self._weight == other._weight
            
    def __ne__(self, other):
        return self._weight != other._weight
        
    def __lt__(self, other):
        return self._weight < other._weight
        
    def __le__(self, other):
        return self._weight <= other._weight
        
    def __gt__(self, other):
        return self._weight > other._weight
        
    def __ge__(self, other):
        return self._weight >= other._weight
        
    def __str__(self):
        string = 'Directed edge coming from vertex ' + str(self._from_vert) + ' to vertex ' + str(self._towards_vert) + ' with a weight of: ' + str(self._weight) 
        return string


def main():
    v = int(sys.argv[1])
    w = int(sys.argv[2])
    weight = float(sys.argv[3])
    
    edge_1 = Directed_Edge(v,w,weight)
    
    print(edge_1.weight())
    print(edge_1.from_vert())
    print(edge_1.towards_vert())
    
    print(edge_1)

if __name__=="__main__": main()