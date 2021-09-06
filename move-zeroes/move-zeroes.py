class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return num
        
        left = 0
        right = 0
        
        while left < len(nums):
            if nums[left] == 0:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1 
                right += 1
            
        return nums
        