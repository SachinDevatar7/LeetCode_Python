class Solution(object):
    def longestPalindrome(self, s):
        if not s or len(s) == 0:
            return s
        
        res = ''
        for i in range(len(s)):
            odd = self.helper(s, i, i)
            even = self.helper(s, i, i+ 1)
            
            res = max(odd, even, res, key = len)
            
        return res
    
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return s[left+1 : right]
    
    
    
    
    
    
    
    
    





















 #length = len(s)
        
#         def expand_center(i,j):
#             while i>=0 and j < len(s) and s[i] == s[j]:
                
#                 i -= 1
#                 j += 1 
                
#             return s[i + 1 : j]
        
#         result = ''
        
#         for i in range(length):
#             temp_palin = expand_center(i,i) # odd

#             if len(temp_palin) > len(result):
#                 result = temp_palin
        
#             temp_palin = expand_center(i, i+ 1) # even 

#             if len(temp_palin) > len(result):
#                 result = temp_palin
            
#         return result
            
        
        
        