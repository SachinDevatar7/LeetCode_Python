class Solution(object):
    def countSubstrings(self, s):
        if len(s) == 0:
            return 0
        
        n = len(s)
        count = 0
        dp = [[False] * n for i in range(len(s))]
        # print(dp)
        
        for i in range(len(s)):
            dp[i][i] = True
            count += 1
            
            # avoid one for loop (len(s) - 1)
            if i + 1 < n and s[i] == s[i + 1]: # i + 1 < n since s[i + 1] is check every stage
                dp[i][i+1] = True
                count += 1
                
        for sLen in range(3, len(s) + 1):
            for i in range(0, n-sLen + 1):
                j = i + sLen - 1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                             
        return count
                
        
                
        
        
        