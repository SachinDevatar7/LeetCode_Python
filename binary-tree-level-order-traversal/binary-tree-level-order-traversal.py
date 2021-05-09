# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Why temp? 
# The value should be in list of list as we go so we are taking a help of temp to store each level and finally put that in result as list(temp)

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #Time and space is O(N)
        if root == None:
            return None
        
        queue = deque()
        queue.append(root)
        result = []
        temp = []
        temp.append(root.val)
        
        while queue:
            queue_len = len(queue)
            result.append(list(temp))
            for i in range(queue_len):
                node = queue.popleft()
                # Missed temp.pop()
                temp.pop(0)
                
                if node.left != None:
                    queue.append(node.left)
                    temp.append(node.left.val)
                    # result.append(list(node.left.val)) int object is not iteratable 
                  
                    
                if node.right != None:
                    queue.append(node.right)
                    temp.append(node.right.val)
                    #result.append(list(node.right.val))
            
        return result
                    
        
            
                    
            