class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0
        for letter in t :
            if counter == len(s):
                break 
            if s[counter] == letter:
                counter +=1 
        return counter ==len(s)   
         


        