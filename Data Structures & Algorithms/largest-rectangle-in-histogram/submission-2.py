class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        counter = 0
        height2 =[]
        pop =False 
        for i in heights :
            while stack and stack[-1][0]> i :
                height2.append((counter-stack[-1][1])*stack[-1][0])
                t =stack[-1][1]
                pop =True 
                stack.pop()
            if pop :
                stack.append((i,t))
                pop =False
            else:
                stack.append((i,counter))
            counter +=1
        while stack:
            height2.append((counter-stack[-1][1])*stack[-1][0])
            stack.pop()
        return max(height2)




        