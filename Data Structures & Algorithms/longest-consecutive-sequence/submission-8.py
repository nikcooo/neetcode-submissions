class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        a =0
        b = 0
        for n in num:
            if (n-1) not in num:
                a = 0
                while  (n+a) in num :
                    a +=1
                    b = max(a,b)
        return b
        
        


        