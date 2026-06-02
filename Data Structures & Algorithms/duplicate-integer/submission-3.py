class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        t = 0
        while t < len(nums)-1:
            dict[nums[t]]= t
            t=t+1
            if nums[t] in dict:
                return True
        return False

 
