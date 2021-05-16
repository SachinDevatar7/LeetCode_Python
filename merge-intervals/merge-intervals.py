class Solution(object):
    def merge(self, intervals):
        if not intervals or len(intervals) == 0:
            return []
        
        intervals.sort(key = lambda x:x[0])
        result = []
        
        for interval in intervals:
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result
        