class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        numViolation = 0
        
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                
                if numViolation == 1:
                    return False
                
                numViolation += 1
                
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                    
        return True
                
        