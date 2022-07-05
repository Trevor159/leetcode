class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        neighbors = {}
        ans = 0
        
        for num in nums:
            
            if num in neighbors:
                continue
            
            left = num
            right = num
            
            if num-1 in neighbors:
                left = neighbors[num-1][0]
                
            if num+1 in neighbors:
                right = neighbors[num+1][1]
                
            neighbors[left] = (left, right)
            neighbors[right] = (left, right)
            neighbors[num] = (left, right)
                
            ans = max(ans, right-left + 1)
            
        return ans
        
        
        