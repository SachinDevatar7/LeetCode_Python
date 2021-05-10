# time : O(n^2 n logn)
# Space: O(N)
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or len(nums1) == 0 or len(nums2) == 0:
            return []
        
        res = []
        for number1 in nums1:
            for number2 in nums2:
                res.append([number1, number2])
        
        res = sorted(res, key = lambda x:x[0] + x[1])
        return res[:k]