class Solution:
    def sumBase(self, n: int, k: int) -> int:
        summ = 0
        while n > 0:
            summ += n % k
            n = n // k
        return summ
        