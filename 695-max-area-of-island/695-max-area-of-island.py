class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ans = 0
        M = len(grid)
        N = len(grid[0])
        
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        
        def processNode(x, y):
            if x < 0 or y < 0 or x >= M or y >= N or grid[x][y] == 0:
                return 0
            
            ret = 1
            grid[x][y] = 0
            
            for xdiff, ydiff in dirs:
                newx = x + xdiff
                newy = y + ydiff
                
                ret += processNode(newx, newy)
                
            return ret
        
        for x in range(M):
            for y in range(N):
                ans = max(ans, processNode(x, y))
                
        return ans
        