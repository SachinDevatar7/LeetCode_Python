class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        
        while n != 0:
            if n != 1 and n % 3 != 0:
                return False
            else:
                n = n//3
                
        return True
        