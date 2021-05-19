class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        
        p_left = 0
        p_right = 0
        
        while p_left < len(s) and p_right < len(t):
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1
            
        if len(s) == p_left:
            return True
        return False
        