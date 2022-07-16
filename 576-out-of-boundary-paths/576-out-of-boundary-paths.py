class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        mod = 10 ** 9 + 7
        
        
        @cache
        def processPos(x, y, movesLeft):
            if x == -1 or x == m or y == -1 or y == n:
                return 1
            
            if movesLeft == 0:
                return 0
            
            ret = 0
            
            for xdiff, ydiff in dirs:
                newx = x + xdiff
                newy = y + ydiff
                
                ret += processPos(newx, newy, movesLeft-1)
                
            return ret % mod
        
        return processPos(startRow, startColumn, maxMove)
            
        
        