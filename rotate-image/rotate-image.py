class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Time and Space complexity: O(n^2) and O(1) rotatate in place
        n = len(matrix[0])
        
        for row in range(n):
            for col in range(row,n):
                matrix[col][row], matrix[row][col] = matrix[row][col],matrix[col][row]
                
        for row in range(n):
            matrix[row].reverse()
            
        #https://www.youtube.com/watch?v=kd5u3GEQkPY&ab_channel=thecodingworld
        