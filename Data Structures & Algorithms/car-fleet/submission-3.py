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
                while  time >= stack[-1]:
                    stack.pop()
                    if not stack:
                        break
                stack.append(time) 
            else :
                stack.append(time)
        return len(stack)
       





        