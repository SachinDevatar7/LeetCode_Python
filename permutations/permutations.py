class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        result = []
        self.backtrack(result, visited, [], nums)
        return result
    
    def backtrack(self, result, visited, subset, nums):
        if len(subset) == len(nums):
            result.append(subset)
        
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtrack(result, visited, subset +[nums[i]], nums)
                visited.remove(i)
        
        

        
#https://leetcode.com/problems/permutations/discuss/360280/Python3-backtracking