class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        
        n = len(nums)
        median = 0
        # find median
        if len(nums) % 2 == 0:
            median = (nums[n//2] + nums[n//2-1]) /2 
        else:
            median = nums[n//2]
        
        # calculate steps
        steps = 0
        for num in nums:
            steps += abs(num - median)
        
        return int(steps)
        
            
        
        