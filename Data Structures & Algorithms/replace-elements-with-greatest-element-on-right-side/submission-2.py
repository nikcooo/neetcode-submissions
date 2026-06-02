class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        x = len(arr)-2
        ans = [-1]*len(arr)
        issupp = arr[len(arr)-1]
        while x >= 0 :
            if issupp < arr [x]:
                ans[x] = issupp
                issupp =arr[x]
                
            else :
                ans[x] = issupp
            x -= 1
        return ans 


        