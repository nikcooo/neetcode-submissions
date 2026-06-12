class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s)-1
        s =s.lower()
        while right >= left :
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[left] == s[right]:
                        left +=1 
                        right -=1
                    else:
                        return False
                else :
                    right -=1
            else:
                left += 1
            if left >len(s)-1 :
                break
            
        return True


