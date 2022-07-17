class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        slices = defaultdict(list)
        ans = [0] * len(queries)
        
        
        for i in range(len(queries)):
            k, trim = queries[i]
            slices[trim].append((i, k))
            
        for trim in slices:
            ordered = sorted([(nums[i][-trim:], i) for i in range(len(nums))])
            
            for index, k in slices[trim]:
                
                ans[index] = ordered[k-1][1]
                
        return ans
            