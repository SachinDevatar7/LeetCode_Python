class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key = lambda courses:(courses[1]))
        print(courses)
        maxHeap = []
        
        time = 0
        
        # course[0] --> Duration
        # course[1] --> Lastday
        for course in courses:
            if course[0] <= course[1]:
                if time + course[0] <= course[1]:
                    heapq.heappush(maxHeap, -course[0])
                    time += course[0]
                    #print(maxHeap)
                elif maxHeap and -maxHeap[0] > course[0]:
                    course[1] = -heapq.heappop(maxHeap)
                    time = time - course[1] + course[0]
                    heapq.heappush(maxHeap, -course[0])
                    
       
        return len(maxHeap) 
        