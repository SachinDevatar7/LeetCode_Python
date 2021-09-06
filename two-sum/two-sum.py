class Solution(object):
    def twoSum(self, nums, target): 
        if len(nums) <= 0:
            return False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        
        
        
        
#         dic = {}
        
#         for i in range(len(nums)):
#             if nums[i] not in dic:
#                 dic[target - nums[i]] = i
#             else:
#                 return dic[nums[i]], i
            
                