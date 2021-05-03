 #Time and Space is O(N) and O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        result = [0] * len(nums)
        result[0] = 1
        
        rp = 1
        # forward pass
        for i in range(1, length):
            rp = rp * nums[i-1]
            result[i] = rp
            
        rp = 1
        # backward pass
        for i in reversed(range(length - 1)):
            rp = rp * nums[i + 1]
            result[i] = result[i] * rp
            
        return result
