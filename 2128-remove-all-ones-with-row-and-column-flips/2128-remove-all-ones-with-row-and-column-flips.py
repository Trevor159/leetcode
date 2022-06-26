class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        r1 = grid[0]
        inverse = [1-x for x in r1]
        N = len(grid)
        for i in range(1, N):
            if grid[i] != r1 and grid[i] != inverse:
                return False
            
        return True