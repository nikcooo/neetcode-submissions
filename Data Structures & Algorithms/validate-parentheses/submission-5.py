class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for element in s :
            if element =="("  or element == "[" or element =="{":
                stack.append(element)
            elif len(stack) == 0:
                return False
            elif element ==")" and stack[-1] =="(" or element == "]"and stack[-1] =="[" or element =="}" and stack[-1] =="{":
                stack.pop()
            else :
                return False
        if   len(stack) == 0:
            return True
        else:
            return False



        