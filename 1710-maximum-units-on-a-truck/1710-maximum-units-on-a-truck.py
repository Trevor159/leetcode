class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        # print(boxTypes)
        ans = 0
        for boxes, units in boxTypes:
            if truckSize == 0:
                break
                
            amount = min(truckSize, boxes)
            ans += amount * units
            truckSize -= amount
            
        return ans