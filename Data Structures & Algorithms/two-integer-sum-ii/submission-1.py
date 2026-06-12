class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        slowpointer = 0
        fastpointer = 1
        while target !=(numbers[slowpointer]+numbers[fastpointer]):
            fastpointer +=1
            if fastpointer > len(numbers)-1:
                slowpointer +=1
                fastpointer = slowpointer +1
            else :
                continue 
        result.append(slowpointer+1)
        result.append(fastpointer+1)
        return result


            

        