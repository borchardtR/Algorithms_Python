# Title: bruteforce_backtracking.py
# Author: Ryan Borchardt


# Time complexities:
    # ~N in typical cases
    # M in the best case (very unlikely)
    # ~M*(N-M+1) = ~M*N in the worst-case

# Space complexities:
    # constant in all cases.


# Example:
# python bruteforce_backtracking.py

def search(text, pattern):
    N = len(text)
    M = len(pattern)
    i=0
    j=0
    
    # some sort of loop
    while True:
        # if i reaches N, then we have examined every character in the text and have unsuccsefully found the pattern
        if i > N:
            return N
        # if j reaches M, then we know we have found the pattern in the text. returns the index for the first character of the pattern in the text.
        # shouldn't this be i-M
        elif j == M:
            return i-M
        # if the character at text[i] matches the character at pattern[j], we might have the pattern, increment both pointers in order to compare the next corresponding characters
        elif text[i] == pattern[j]:
            i += 1
            j += 1
        # if the character at text[i] does NOT equal the character at pattern[j], we know that the pattern doesn't exist starting at index i-j of the text.  
            # reset the pointer j to 0.
            # backtrack the pointer i to the next starting index in text (set i to i-j+1)
        elif text[i] != pattern[j]:
            i = i - j + 1
            j = 0

    
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