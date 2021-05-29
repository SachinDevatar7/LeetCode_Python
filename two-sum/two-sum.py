class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 0:
            return False
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[target - nums[i]] = i
            else:
                return dic[nums[i]], i
        
        
        
        
        
        
        
        
        
        
        
# https://www.youtube.com/watch?v=U8B984M1VcU&feature=youtu.be

