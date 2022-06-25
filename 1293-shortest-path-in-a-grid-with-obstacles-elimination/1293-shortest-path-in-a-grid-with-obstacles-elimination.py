class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        M = len(grid)
        N = len(grid[0])
        
        queue = deque()
        queue.append((0, 0, 0, 0))
        seen = {}
        
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        
        while queue:
            x, y, steps, obstacles = queue.popleft()
            
            obstacles += grid[x][y]
            
            if x == M-1 and y == N-1:
                return steps
            
            if obstacles > k:
                continue
                
            if (x,y) in seen and seen[(x,y)] <= obstacles:
                continue
                
            seen[(x,y)] = obstacles
            
            
            steps += 1
            
            for xdiff, ydiff in dirs:
                newx = x + xdiff
                newy = y + ydiff
                
                if newx < 0 or newy < 0 or newx >= M or newy >= N:
                    continue
                    
                queue.append((newx, newy, steps, obstacles))
                
        return -1
            