class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladderAllocate = [] # minHeap
        
        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            
            if diff <= 0:
                continue    
            heapq.heappush(ladderAllocate, diff)
            
            if len(ladderAllocate) > ladders:   
                bricks -= heapq.heappop(ladderAllocate)
                
            if bricks < 0:
                return i
            
        return len(heights) - 1
            