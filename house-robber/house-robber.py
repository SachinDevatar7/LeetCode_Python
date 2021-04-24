class Solution(object):
    def rob(self, nums):
        nt_choose, choose= 0, 0 
        for num in nums:
            nt_choose, choose = max(nt_choose, choose), num + nt_choose
        return max(nt_choose, choose)
        