class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        points = sum(cardPoints[:k])
        ans = points
        N = len(cardPoints)
        
        for i in range(k):
            points += cardPoints[N-1-i]
            points -= cardPoints[k-1-i]
            ans = max(ans, points)
            
        return ans