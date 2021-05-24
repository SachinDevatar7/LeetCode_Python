# Definition for a binary tree node.
# class TreeNode():
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution():
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # recursive solution
        # in Python root is not None or root is same and stack ( run till not empty)
        if root == None:
            return True
        stack = []
        prev = None
        while root or stack: #check until root and stack is not empty
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            # only check if prev is not equal to none
            if prev and root.val <= prev.val:
                return False
            prev = root
            root = root.right
            
        return True
            
        
        