class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # base condition
        if not height or len(height) == 0:
            return height
        
        left = 0
        right = len(height) - 1
        area = 0
        
        # Two Pointer Approach
        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return area
        
        
        