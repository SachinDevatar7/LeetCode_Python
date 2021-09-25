class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        def num_missing(i):
            return nums[i] - nums[0] - i 
        
        low = 0
        high = len(nums)
        
        while low < high:
            mid = (low + high) // 2
            if num_missing(mid) < k: 
                low = mid + 1
            else:
                high = mid
                
        return nums[low-1] + k - num_missing(low - 1)