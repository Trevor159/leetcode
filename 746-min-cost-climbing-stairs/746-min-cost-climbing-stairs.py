class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        curr = nx = 0
        
        for cost in costs:
            temp = curr + cost
            nx = min(nx, temp)
            
            curr, nx = nx, temp
            
            
        return curr