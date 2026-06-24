class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1
        currentmin = min(nums[left],nums[right])
        while left < right :
            mid = (left+right)//2
            if nums[mid] >= nums[left]  :
                left = mid +1   
            elif nums[mid] <= nums[right]:
                right =mid -1 
            currentmin = min(currentmin,nums[mid],nums[left],nums[right])
        return currentmin
            
        