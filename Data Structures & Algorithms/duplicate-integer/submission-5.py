class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Dup = []
        for num in nums :
            if num in Dup :
                return True 
            Dup.append(num)
        return False


        