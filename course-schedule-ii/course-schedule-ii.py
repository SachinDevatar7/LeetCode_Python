class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        queue = []
        result = []
        dic = collections.defaultdict(list)
        degree = [0] * numCourses
        
        for course,precourse in prerequisites:
            dic[precourse].append(course)
            degree[course] += 1
        # print(dic)
        # print(degree)
        
        for i in range(len(degree)):
            if degree[i] == 0:
                queue.append(i)
        
        while queue:
            courseNumber = queue.pop(0)
            result.append(courseNumber)
            
            dicvalue= dic[courseNumber]
            
            for nextcourse in dicvalue:
                degree[nextcourse] -= 1
                
                if degree[nextcourse] == 0:
                    queue.append(nextcourse)
                    
        if len(result) == numCourses:
            return result
        else:
            return []
        