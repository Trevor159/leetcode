class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        numsDivide.sort()
        ans = 0
        
        minDivide = min(numsDivide)
        for i in range(len(nums)):
            num = nums[i]
            
            if num > minDivide:
                return -1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            divides = True
                
            for j in range(len(numsDivide)):
                if j > 0 and numsDivide[j] == numsDivide[j-1]:
                    continue
                    
                if numsDivide[j] % num != 0:
                    divides = False
                    break
                    
            if divides:
                return i
                    
        return -1
                
                
            
        
        
        
        