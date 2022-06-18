class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        colMap = defaultdict(set)
        rowMap = defaultdict(set)
        
        N = len(stones)
        for i in range(N):
            x, y = stones[i]
            colMap[y].add(i)
            rowMap[x].add(i)
            
            
        graph = defaultdict(list)
        
        for i in range(N):
            x, y = stones[i]
            
            for node in colMap[y]:
                if node == i:
                    continue
                    
                graph[i].append(node)
                
            for node in rowMap[x]:
                if node == i:
                    continue
                    
                graph[i].append(node)
                
        
        seen = set()
        ans = N
        
        def seeConnected(node):
            if node in seen:
                return 
            
            seen.add(node)
            
            for neighbor in graph[node]:
                seeConnected(neighbor)
        
        for i in range(N):
            if i in seen:
                continue
            
            ans -= 1
            seeConnected(i)
                
        return ans
                
                
                
                
                
                
                
                
        
        
        
        