class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        N = len(nums)
        changed = False
        
        for i in range(1, N):
            left = nums[i-1]
            # right = nums[i+1] if i != N-1 else math.inf
            val = nums[i]
            
            if left <= val:
                continue
                
                
            if changed:
                return False
            
            changed = True
            if i < 2 or nums[i-2] <= val:
                nums[i-1] = val
            else:
                nums[i] = nums[i-1]
            
        return True