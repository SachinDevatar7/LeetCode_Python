class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        val = 0
        out = []
        for (x,y) in points:
            val = (x ** 2 ) + ( y **2)
            heapq.heappush(heap,(val, [x,y]))
 
        print(heap)
        
        for each in range(k):
            out.append(heapq.heappop(heap)[1])
        return out
        