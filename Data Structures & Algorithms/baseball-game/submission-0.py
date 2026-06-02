class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ans = 0
        for num in operations :
            if num == "+":
                add = stack[-1] + stack[-2]
                stack.append(add)
            elif num =="C":
                stack.pop()
            elif num == "D":
                multiply =stack[-1]*2
                stack.append(multiply)
            else:
                stack.append(int(num))
        for i in stack :
            ans += i
        return ans 

        


                

        