class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [0]
        for asteroid in asteroids:
                while stack[-1] < abs(asteroid) and stack[-1] > 0 and asteroid <0:
                    stack.pop()
                    if len(stack) == 1 and stack[-1] < abs(asteroid) and stack[-1] > 0 and asteroid <0:
                        stack.pop()
                        stack.append(asteroid)
                        pass
                if stack[-1] == -asteroid and stack[-1] > 0 :
                    stack.pop()
                    pass
                elif stack[-1] > asteroid and stack[-1] > 0 and asteroid < 0:
                    pass
                else :
                    stack.append(asteroid)
        if stack[0] == 0:
            stack.pop(0)
        return stack
            
        