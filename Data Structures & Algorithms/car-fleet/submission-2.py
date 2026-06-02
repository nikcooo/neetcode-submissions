class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack =[]
        sorteed =[]
        counter = 0
        for i in  position :
            sorteed.append((i,speed[counter]))
            counter +=1
        sorteed.sort()
        for i in sorteed:
            time = (target - i[0]) / i[1]
            if stack:
                while stack[-1][0] < i[0] and time >= stack[-1][1]:
                    stack.pop()
                    if not stack:
                        break
                stack.append((i[0],time)) 
            else :
                stack.append((i[0],time))
        return len(stack)
       





        