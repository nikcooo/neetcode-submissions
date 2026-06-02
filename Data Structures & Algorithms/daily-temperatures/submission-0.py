class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        stack2 = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            stack.append((temp,i))
            if len(stack) >= 2:
                while stack[-1][0]> stack[-2][0]:
                    stack2[stack[-2][1]] = stack[-1][1]- stack[-2][1]
                    stack.pop(-2)
                    if len(stack) == 1:
                        break
        return stack2
        