class Solution(object):
    def findItinerary(self, tickets):
        self.adjList = collections.defaultdict(list)
        
        tickets.sort(key = lambda x:x[1]) # since we need to maintain lexigraphical order we need it
        print(tickets)
        for start, end in tickets:
            if start not in self.adjList:
                self.adjList[start] = [end]
            else:
                self.adjList[start].append(end)
                
        self.result = []
        self.dfs("JFK")
        return self.result[::-1]
    
    def dfs(self, s):
        while s in self.adjList and len(self.adjList[s]) > 0:
            value = self.adjList[s][0]
            self.adjList[s].pop(0)
            self.dfs(value)
            
        self.result.append(s)

        
        
        