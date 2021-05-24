class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
          # base 
        if not board or len(board) == 1:
            return 
        m = len(board)
        n = len(board[0])

        # if len is <= 2 don't do anything
        if m <= 2: return
        if n <= 2: return
                        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i == 0 or i == m - 1 or j == 0 or j == n-1):
                    self.dfs(board, i, j)
        #print(board)                
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"
    
    def dfs(self, board, i, j):
        if i >= 0 and j >= 0 and i < len(board) and j < len(board[0]) and board[i][j] == "O":
            board[i][j] = "A"
            directions = [(-1, 0), (1,0), (0,1), (0, -1)]
            for dir in directions:
                r = dir[0] + i
                c = dir[1] + j
                self.dfs(board, r, c)
            # self.dfs(board, i+1 , j)
            # self.dfs(board, i-1 , j)
            # self.dfs(board, i , j + 1)
            # self.dfs(board, i , j - 1)
               
        