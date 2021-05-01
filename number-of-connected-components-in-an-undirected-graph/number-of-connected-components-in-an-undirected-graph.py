class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visit = [0] * n
        print(visit)
        
        connected_components = 0
        
        # give the connected edge as value and key as node
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        print(graph)
        
        queue = deque()
        for i in range(n):
            #print(i)
            print(visit[i])
            if visit[i] == 0:
                queue.append(i)
               # print(queue)
                while queue:
                    curr = queue.popleft()
                    #print(curr)
                    visit[curr] = 1
                    for neighbor in graph[curr]:
                        if visit[neighbor] == 0:
                            queue.append(neighbor)
                            #print(queue)
                connected_components += 1
                
        return connected_components