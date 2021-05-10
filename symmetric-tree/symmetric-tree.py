# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:      
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.helper(root.left, root.right)
    
    def helper(self, rootleft, rootright):
        if rootleft == None or rootright == None:
            return rootleft == rootright
        
        return rootleft.val == rootright.val and self.helper(rootleft.left, rootright.right) and self.helper( rootleft.right, rootright.left) 

        
        



    #https://leetcode.com/problems/symmetric-tree/discuss/33052/Recursive-Python-Solution-~~