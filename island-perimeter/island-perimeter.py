class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        self.perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    
        return self.perimeter
    
   
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0:
            self.perimeter += 1
            return 
        if grid[i][j] == X:
            return 
        # logic
        grid[i][j] = X
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        for dir in directions:
            r = dir[0] + i
            c = dir[1] + j
            self.dfs(grid, r,c )
            
            
            
        
        