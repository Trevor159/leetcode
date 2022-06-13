class Solution:
    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(list)
        
        for i in range(n):
            manager = managers[i]
            
            graph[manager].append(i)
            
        
        stack = [(headID, 0)]
        ans = 0
        
        while stack:
            node, time = stack.pop()
            
            if node not in graph:
                ans = max(ans, time)
                continue
                
            time += informTime[node]
            
            neighbors = graph[node]
            
            for neighbor in neighbors:
                stack.append((neighbor, time))
                
        return ans
            
        