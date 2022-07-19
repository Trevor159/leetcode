class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        M = len(board)
        N = len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def helper(left, x, y, prevdir=None):
            if left == len(word):
                return True
            
            if x < 0 or y < 0 or x >= M or y >= N or word[left] != board[x][y]:
                return False
            
            board[x][y] = "#"
            ans = False
            
            for dir in dirs:
                if prevdir and -prevdir[0] == dir[0] and -prevdir[1] == dir[1]:
                    continue
                
                ans = ans or helper(left + 1, x + dir[0], y + dir[1], dir)
            
            board[x][y] = word[left]
            return ans
        

        for x in range(M):
            for y in range(N):
                if helper(0, x, y):
                    return True
        
        return False