class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        x = len(arr)-1
        ans = [-1]
        issupp = arr[x]
        while x > 0 :
            if issupp > arr [x-1]:
                ans.append(issupp)
            else : 
                ans.append(issupp)
                issupp =arr[x-1]
            x -= 1
        ans.reverse()
        return ans 


        