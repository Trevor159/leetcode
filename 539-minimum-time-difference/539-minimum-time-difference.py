class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def calcSeconds(time):
            return int(time[:2]) * 60 + int(time[3:])
        
        timePoints.sort()
        N = len(timePoints)
        ans = float("inf")
        for i in range(N):
            currTime = calcSeconds(timePoints[i])
            prevTime = calcSeconds(timePoints[i-1])
            
            ans = min(ans, abs(currTime-prevTime), abs(prevTime-1440-currTime))
            
        return ans
            
            