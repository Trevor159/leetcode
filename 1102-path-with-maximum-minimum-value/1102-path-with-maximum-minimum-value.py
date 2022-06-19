class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        M = len(grid)
        N = len(grid[0])
        
        heap = []
        seen = set()
        
        heappush(heap, (-grid[0][0], 0, 0))
        
        while heap:
            minimum, x, y = heappop(heap)
            minimum = -minimum
            
            if (x,y) in seen:
                continue
                
            if x == M-1 and y == N-1:
                return minimum
            
            seen.add((x,y))
            
            for xdiff, ydiff in [[1,0],[-1,0],[0,1],[0,-1]]:
                newx = xdiff + x
                newy = ydiff + y
                
                if newx < 0 or newy < 0 or newx >= M or newy >= N or (newx, newy) in seen:
                    continue
                    
                heappush(heap, (-min(minimum, grid[newx][newy]), newx, newy))
                
        return -1
                
                    
                
        
        
        