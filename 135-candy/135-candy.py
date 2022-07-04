class Solution:
    def candy(self, nums: List[int]) -> int:
        N = len(nums)
        dpright = [1] * N
        
        for i in range(N-2, -1, -1):
            if nums[i] > nums[i+1]:
                dpright[i] = dpright[i+1] + 1
                
                
        dpleft = [1] * N
        for i in range(1, N):
            if nums[i] > nums[i-1]:
                dpleft[i] = dpleft[i-1] + 1
                
                
        ans = 0
        
        for i in range(N):
            ans += max(dpleft[i], dpright[i])
            
        return ans
        
        
        
        