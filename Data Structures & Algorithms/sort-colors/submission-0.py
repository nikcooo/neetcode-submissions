class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0 = 0
        count1 = 0
        count2 = 0
        for n in nums:
            if n == 0:
                count0 += 1
            elif n == 1:
                count1 += 1
            else:
                count2 += 1
        nums[:] = [0]*count0 + [1]*count1 + [2]*count2