# Title: edge.py
# Author: Ryan Borchardt


# Example:
# python edge.py 4 5 0.35


import sys
# Added Algorithms's parent directory to sys.path
sys.path.append('C:/Users/borch/Desktop/Work/github_repository_main/')

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self._weight = weight
    
    def weight(self):
        return self._weight
    
    def either(self):
        return self.v
    
    def other(self, v):
        if v==self.v:
            return self.w
        elif v == self.w:
            return self.v
        else:
            raise Exception("Edge object does not contain inputted vertex.")
    
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
        string = 'Edge connecting vertices: ' + str(self.v) + ' , ' + str(self.w) + ' with a weight of: ' + str(self._weight) 
        return string


def main():
    v = int(sys.argv[1])
    w = int(sys.argv[2])
    weight = float(sys.argv[3])
    
    edge_1 = Edge(v,w,weight)
    
    print(edge_1.weight())
    print(edge_1.either())
    print(edge_1.other(v))
    
    print(edge_1)

if __name__=="__main__": main()