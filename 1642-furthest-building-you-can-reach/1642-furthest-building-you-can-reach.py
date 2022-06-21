class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        brickheap = []
        N = len(heights)
        ans = 0
        
        
        for i in range(1, N):
            diff = heights[i] - heights[i-1]
            
            if diff <= 0:
                continue
        
            # print(diff)
            if diff > bricks and ladders == 0:
                return i-1
            
            ans += 1
            
            if bricks >= diff:
                heappush(brickheap, -diff)
                bricks -= diff
                continue
                
            ladders -= 1
            if not brickheap:
                continue
                
            mostbricks = -brickheap[0]
            
            if diff < mostbricks:
                bricks += mostbricks-diff
                heappop(brickheap)
                heappush(brickheap, -diff)
                
        return N-1
                
                
            