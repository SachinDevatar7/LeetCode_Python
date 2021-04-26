# Check Notes

# Why MinHeap?
# I need a minHeap since I have to get to use min bricks from the pile of given bricks which I get through minHeap so it's pop can be done in O(logn) Time which makes perfect to use minHeap

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # diff are the climb steps to make it which is inside my ladderAllocate
        ladderAllocate = [] # minHeap to keep count of how many ladder used
        
        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            
            if diff <= 0:
                continue    
            heapq.heappush(ladderAllocate, diff)
            #print(ladderAllocate)
            
            # Tell ladder count how many being used 
            if len(ladderAllocate) > ladders: # tells used all ladder and now need to use bricks 
                bricks -= heapq.heappop(ladderAllocate)
                
            #print(bricks)
                
            if bricks < 0:
                return i
            
        return len(heights) - 1
            