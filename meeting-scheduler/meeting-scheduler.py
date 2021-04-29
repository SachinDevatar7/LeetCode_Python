class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        slots1.sort()
        slots2.sort()
        
        p1 = 0
        p2 = 0
        
        while p1 < len(slots1) and p2 < len(slots2):
            # since I should not overlap so min for right and max for left
            interval_right = min(slots1[p1][1], slots2[p2][1])
            interval_left = max(slots1[p1][0], slots2[p2][0])
                                
            if (interval_right - interval_left) >= duration: # tells the overlap
                return [interval_left, interval_left + duration]
                                
            if slots1[p1][1] < slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return []
                                
            
        
        