#https://www.youtube.com/watch?v=Y0ZqKpToTic&ab_channel=TusharRoy-CodingMadeSimpleTusharRoy-CodingMadeSimple

# Single array!
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Base Case
        if not coins or len(coins) == 0:
            return 0
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1): # start with coin previous coin
                dp[i] = min(dp[i-coin] + 1, dp[i])
            
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
        
 