class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        result = 0
        curentleftmax = height[left]
        curentrightmax = height[right]
        
        while right> left :
            if curentleftmax >= height[right]:
                maxloc = height[right]
                while (curentleftmax >= height[right]) and right> left :
                    if maxloc <height[right]:
                        maxloc =height[right]
                    elif maxloc-height[right]>= 0 :
                        result += maxloc-height[right]
                    right -=1
                curentrightmax = height[right]
            elif height[left] < curentrightmax:
                maxloc = height[left]
                while (height[left] < curentrightmax) and right> left :
                    if maxloc <height[left]:
                        maxloc =height[left]
                    elif maxloc-height[left]>= 0 :
                        result += maxloc-height[left]
                    left +=1
                curentleftmax = height[left]
        return result 