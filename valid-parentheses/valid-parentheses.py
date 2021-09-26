class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) % 2 != 0: # Odd Case so return False
            return False
        
        stack = []
        
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '{':
                stack.append('}')
            elif i == '[':
                stack.append(']')
            elif not stack or i != stack.pop():
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False
        