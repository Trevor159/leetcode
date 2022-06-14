class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        N1 = len(word1)
        N2 = len(word2)
        
        @cache
        def backtrack(index1, index2):
            
            if (index1 == N1) and (index2 == N2):
                return 0
            
            if index1 == N1:
                return backtrack(index1, index2+1) + 1
            
            if index2 == N2:
                return backtrack(index1+1, index2) + 1
            
            ans = inf
            if word1[index1] == word2[index2]:
                ans = backtrack(index1+1, index2+1)
            ans = min(ans, backtrack(index1+1, index2) + 1)
            ans = min(ans, backtrack(index1, index2+1) + 1)
            
            return ans
            
        return backtrack(0, 0)
                
                
        
        
        
        