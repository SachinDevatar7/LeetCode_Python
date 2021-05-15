class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Time and Space Complexity: O(N) and O(1)
        left = 0
        right = len(height) - 1
        area = 0
       
        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            
            #need maximum so increament left if left is less than right
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return area
            