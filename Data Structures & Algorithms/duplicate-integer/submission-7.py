class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Dup = {}
        for num in nums :
            if num not in Dup :
                Dup[num]=1
            else :
                return True 
        return False


        