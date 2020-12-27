# Title: kmp.py
# Author: Ryan Borchardt


# Example:
# python kmp.py


class KMP:
    def __init__(self, pattern):
        self.pattern = pattern
        # build dfa table...
        R = 256
        self.dfa = [[0]*len(self.pattern)]*R

    def search(self, text):
        N = len(text)
        M = len(self.pattern)
        i=0
        j=0
    
        
        while True:
        
            # if i reaches N, then we have examined every character in the text and have unsuccsefully found the pattern
            if i >= N:
                return N
        
            j = dfa[ord(text[i])][j]
        
        
            # if j reaches M, then we know we have found the pattern in the text. returns the index for the first character of the pattern in the text.
            # shouldn't this be i-M
            elif j == M:
                return i-M
        
    
            i += 1
  
        

    
def main():
    text1 = "ABACADABRAC"
    pat1 = "ABRA"
    
    text2 = "AAAAAAAAAB"
    pat2 = "AAAAB"
    
    x = search(text1, pat1)
    print('n: ', len(text1))
    print('m: ', len(pat1))
    print(x)
    
    y = search(text2, pat2)
    print('n: ', len(text2))
    print('m: ', len(pat2))
    print(y)
   
    
if __name__=="__main__": main()