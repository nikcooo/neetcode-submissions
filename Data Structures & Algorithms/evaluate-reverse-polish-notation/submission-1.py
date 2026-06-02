class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for element in tokens :
            if element in ["+", "/", "-" , "*"]:
                a = int(stack[-2])
                b = int(stack[-1])
                stack.pop()
                stack.pop()
                if element == "+":
                    c = a+b
                elif element == "-":
                    c = a-b
                elif element == "*":
                    c=a*b
                elif element == "/":
                   c = int(a/b)
                    
                stack.append(c)   
            else:
                stack.append(element)
        return int(stack[0])