class Solution:
    def candy(self, nums: List[int]) -> int:
        N = len(nums)
        dpright = [1] * N
        
        for i in range(N-2, -1, -1):
            if nums[i] > nums[i+1]:
                dpright[i] = dpright[i+1] + 1
        
        ans = dpright[0]
        prev = 1

        for i in range(1, N):
            if nums[i] > nums[i-1]:
                prev = prev + 1
            else:
                prev = 1
                
            ans += max(dpright[i], prev)
                
            
        return ans
        
        
        
        