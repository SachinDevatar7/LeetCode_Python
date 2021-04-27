# Stack [LIFO] so why we are using is in order to process it as a pair we are using stack! with usage of stack you can keep track of each VALID Pair!

class Solution(object):
    def isValid(self, s):
        if not s or len(s) % 2 != 0:
            return False
        
        stack = []
        
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            elif not stack or i != stack.pop():
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False
            
            
        
        
        