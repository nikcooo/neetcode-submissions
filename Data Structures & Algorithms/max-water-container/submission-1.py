class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left =0
        right = len(heights)-1
        currentmaxleft = 0 
        currentmaxright =-1 
        result = 0
        while right > left :
            if currentmaxright >= currentmaxleft:
                if currentmaxleft < heights[left]:
                    currentmaxleft = heights[left]
                    if result < min(heights[left],heights[right])*(right - left):
                        result = min(heights[left],heights[right])*(right - left)
                else:
                    left +=1
            elif currentmaxright <= currentmaxleft:
                if currentmaxright < heights[right]:
                    currentmaxright = heights[right]
                    if result < min(heights[left],heights[right])*(right - left):
                        result = min(heights[left],heights[right])*(right - left)  
                else :
                    right -=1
        return result 
               
        