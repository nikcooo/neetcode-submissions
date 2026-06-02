class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        a = 1
        b = 1
        t =0
        t2 = 0
        for i in range(len(nums)):
            dict[nums[i]] = nums[i]+1
        if dict == {} :
            return 0 
        while t < len(nums):
            t2 = nums[t]
            if dict.get(nums[t]-1) is not None:
                t +=1
            else :
                b =0
                while dict.get(t2+1) is not None :
                    b +=1
                    t2 +=1 
                    if a <= b:
                        a = b 
                        a +=1  
                t +=1
        
        return a
        
        


        