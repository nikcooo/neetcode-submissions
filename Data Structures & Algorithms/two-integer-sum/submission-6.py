from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionaire = defaultdict(list)
        counter =0
        for num in nums :
            dictionaire[num].append(counter)
            x = target - num
            if x in dictionaire : 
                if dictionaire.get(x)[0]!=dictionaire.get(num)[-1] :
                    return [dictionaire.get(x)[0],dictionaire.get(num)[-1]]
            counter +=1
        return counter 


        