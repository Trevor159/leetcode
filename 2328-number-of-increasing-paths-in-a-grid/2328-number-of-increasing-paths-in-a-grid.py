class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        M = len(grid)
        N = len(grid[0])
        
        @cache
        def processPos(x, y):
            val = grid[x][y]
            ret = 1
            
            for xdiff, ydiff in dirs:
                newx = x + xdiff
                newy = y + ydiff
                
                if newx < 0 or newy < 0 or newx >= M or newy >= N or grid[newx][newy] <= val:
                    continue
                    
                ret += processPos(newx, newy)
                
            return ret
        
        ans = 0
        
        for x in range(M):
            for y in range(N):
                ans += processPos(x, y)
                
        return ans % ((10 ** 9) + 7)
                
                
