class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if not n or n == None:
            return False
        
        while n != 0:
            if n != 1 and n % 2 != 0:
                return False
            else:
                n = n // 2
                
        return True
        