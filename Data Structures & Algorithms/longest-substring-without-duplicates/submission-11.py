
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointer1 =0
        pointer2 =0
        lenght = 0 
        dictionary = {}
        dicti = False
        while pointer1 < len(s):
            if s[pointer1] in dictionary:
                if dictionary[s[pointer1]] >= pointer2:
                    pointer2 = dictionary[s[pointer1]] +1 
                    dicti = True 
            dictionary[s[pointer1]] = pointer1       
            lenght = max(lenght,pointer1 - pointer2)
            pointer1 +=1
        if dicti :
            return lenght +1
        else :
            return len(s)
            