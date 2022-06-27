class Solution:
    def minPartitions(self, n: str) -> int:
        ans = n[0]
        
        for i in range(1, len(n)):
            char = n[i]
            ans = max(ans, char)
            
        return max(1, int(ans))