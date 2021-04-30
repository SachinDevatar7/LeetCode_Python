# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self,left, right):
        if left == None or right == None:
            return left == right
        # elif (left is None and right) or (left and right is None):
        #     return False
        # elif left.val != right.val:
        #     return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(right.left,  left.right)