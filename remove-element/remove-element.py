class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # TO DO NOW
        count = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count
        