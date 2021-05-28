# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        
        if not root:
            return None
        
        queue = deque()
        queue.append(root)
        temp = []
        temp.append(root.val)
        result = []
        
        while queue:
            result.append(list(temp))
            for i in range(len(queue)):
                curr = queue.popleft()
                temp.pop(0)
                
                if curr.left != None:
                    queue.append(curr.left)
                    temp.append(curr.left.val)
                    
                if curr.right != None:
                    queue.append(curr.right)
                    temp.append(curr.right.val)
                    
        return result
                
                
        
        