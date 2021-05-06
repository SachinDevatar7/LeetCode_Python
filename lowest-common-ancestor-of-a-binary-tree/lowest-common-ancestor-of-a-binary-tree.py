# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # Base case
        if root == None or root == p or root == q:
            return root
        
        
        # Logic
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # processing flags
        if left != None and right != None:
            return root
        elif left != None:
            return left
        elif right != None:
            return right
        else:
            return None
        