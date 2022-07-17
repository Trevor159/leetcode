class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        ans = -1
        
        maxes = {}
        
        for num in nums:
            digitsum = 0
            temp = num
            
            while temp:
                digitsum += temp % 10
                temp //= 10
                
            # print(nu)
                
            if digitsum in maxes:
                ans = max(ans, num + maxes[digitsum])
                maxes[digitsum] = max(maxes[digitsum], num)
            else:
                maxes[digitsum] = num
                
        return ans
                
        
        
        