class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        slowpointer = 0
        fastpointer = len(numbers)-1
        while target != (numbers[slowpointer]+numbers[fastpointer]):
            if target >(numbers[slowpointer]+numbers[fastpointer]):
                slowpointer +=1
            else:
                fastpointer -=1
        result.append(slowpointer+1)
        result.append(fastpointer+1)
        return result


            

        