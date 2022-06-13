class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        left = right = 0
        N = len(nums)
        ans = 0
        mins = deque()
        maxs = deque()
        
        while right < N:
            num = nums[right]
            
            while maxs and num > maxs[-1]:
                maxs.pop()
                
            while mins and num < mins[-1]:
                mins.pop()
                
            maxs.append(num)
            mins.append(num)
            
            while maxs[0]-mins[0] > limit:
                num = nums[left]
                if maxs[0] == num:
                    maxs.popleft()
                elif mins[0] == num:
                    mins.popleft()
                    
                left += 1
            
            
            ans = max(ans, right-left+1)
            right += 1
            
        return ans
        
        
        