class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
        if finalSum % 2 == 1:
            return []
        
        ans = []
        val = 2
        
        while True:
            ans.append(val)
            finalSum -= val
            val += 2
            
            if finalSum < val:
                ans[-1] += finalSum
                break
                
        return ans