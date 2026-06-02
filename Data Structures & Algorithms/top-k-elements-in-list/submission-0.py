from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums).most_common(k)
        a =[x[0] for x in a]
        return a 



        
        