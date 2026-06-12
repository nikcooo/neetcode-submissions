class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        pacepointer,leftpointer,rightpointer = 0,1,len(nums)-1
        result = []
        placeholder = []
        while pacepointer < len(nums)-2:
            while rightpointer > leftpointer:
                if pacepointer == leftpointer:
                    leftpointer+=1
                elif pacepointer == rightpointer:
                    rightpointer -=1
                elif nums[leftpointer] + nums[rightpointer] + nums[pacepointer]==0:
                    placeholder.append(nums[leftpointer])
                    placeholder.append(nums[pacepointer])
                    placeholder.append(nums[rightpointer])
                    if placeholder in result :
                        pass
                    else :
                        result.append(placeholder)
                    placeholder = []
                    leftpointer +=1
                elif 0 < nums[rightpointer] + nums[leftpointer]+nums[pacepointer]:
                    rightpointer -=1
                else :
                    leftpointer +=1
            pacepointer +=1
            leftpointer,rightpointer = pacepointer +1,len(nums)-1
        return result
        