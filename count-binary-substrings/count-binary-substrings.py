# Approach: 
# Find the number of substring with equal number of 0's and 1's 
# take a min(count_zero, count_one) in all substring and add all number that is answer   

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group = [1]
        
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                group.append(1)
            else:
                group[-1] += 1
        result = 0
        for i in range(1, len(group)):
            result += min(group[i-1], group[i])
        return result
        