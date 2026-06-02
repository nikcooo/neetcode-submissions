class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        t = 0
        while t < len(nums):
            a = target - nums[t]
            if a in dict :
                if dict[a] < t :
                    return [dict[a],t]
            dict[nums[t]] = t
            t=t+1




        
        

    
        