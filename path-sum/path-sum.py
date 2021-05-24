# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time Complexity: O(N)
#Space Complexity: O(N)
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # recursion
        return self.helper(root, sum)
    
    
    def helper(self, root, sum_path):
        #Base case
        if not root:
            return False
        
        # logic
        if not root.left and not root.right:
            if sum_path - root.val == 0:
                return True
            return False
        
        return self.helper(root.left, sum_path - root.val) or self.helper(root.right, sum_path - root.val)