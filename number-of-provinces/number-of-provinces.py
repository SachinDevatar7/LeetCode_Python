class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        visited = set()
        counter, n = 0, len(isConnected)
        for i in range(n):
            if i not in visited:
                self.dfs(isConnected, i, visited)
                counter += 1
        return counter

    def dfs(self, isConnected, i, visited):
        visited.add(i)
        for idx, val in enumerate(isConnected[i]):
            if val == 1 and idx not in visited:
                self.dfs(isConnected, idx, visited)
                
        
        