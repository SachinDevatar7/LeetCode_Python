# Check Notes 

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
    
        nums.sort()    
        i = 0
        ops = 0
        
        for j in range(len(nums)):
            
            if j:
                ops += (nums[j] - nums[j-1]) * (j - i)
                
            if ops > k:
                ops -= nums[j] - nums[i]
                i += 1
            
        return j - i + 1
        