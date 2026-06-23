class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left =1
        result =0
        currentresult = max(piles)
        while left <= right :
            mid = (left + right)//2
            for banana in piles :
                if banana % mid != 0:
                    result += (banana //mid) +1
                else :
                    result += (banana //mid)
            if result <= h:
                right = mid -1
            else :
                left = mid +1
            if result <= h:
                currentresult = min(mid,currentresult)
            result = 0
        return currentresult


