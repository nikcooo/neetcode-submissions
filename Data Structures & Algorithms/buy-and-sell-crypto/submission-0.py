class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentbuy = 101
        counter = 0
        result = 0
        while counter < len(prices):
            if prices[counter] < currentbuy :
               currentbuy = prices[counter] 
            result = max(result , (prices[counter]-currentbuy))
            counter +=1
        return result 
        