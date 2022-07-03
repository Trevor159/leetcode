class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = 1
        
        pos = False
        
        index = 1
        
        while index < len(nums) and nums[index] == nums[index-1]:
            index += 1
            
        if index == len(nums):
            return ans
            
        if nums[index] > nums[index-1]:
            pos = True
        
        prev = nums[index-1]
        # print(index)
        
        for i in range(index, len(nums)):
            num = nums[i]
            
            if pos and num > prev:
                ans += 1
                pos = False
                
            if not pos and num < prev:
                ans += 1
                pos = True
                
            prev = num
            
        return ans