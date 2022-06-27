class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        import sortedcontainers
        sort = sortedcontainers.SortedList()
        for i in range(N-1, -1, -1):
            num = nums[i]
            index = sort.bisect_left(num)
            nums[i] = index
            sort.add(num)
            
        return nums