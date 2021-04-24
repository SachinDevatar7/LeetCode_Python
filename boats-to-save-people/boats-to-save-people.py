class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if not people or len(people) == 0:
            return 0
        
        people.sort()
        
        left = 0
        right = len(people) - 1
        count_boat = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                count_boat += 1
            else:
                right -= 1
                count_boat += 1
        return count_boat
        
                
        