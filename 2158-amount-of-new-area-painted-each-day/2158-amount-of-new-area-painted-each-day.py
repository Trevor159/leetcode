class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        records = []
        N = len(paint)
        from sortedcontainers import SortedList
        ans = []
        sort = SortedList()
        for start, finish in paint:
            index = sort.bisect_left((start, finish))
            
            prevstart = start
            val = 0
            if index != 0 and sort[index-1][1] >= start:
                prevstart = sort[index-1][0]
                index -= 1
                start = prevstart
                
            # print(start, finish, index, sort)
            while index < len(sort) and sort[index][0] <= finish:
                currstart, currfinish = sort[index]
                sort.pop(index)
                val += currstart - start
                start = currfinish
                
            if finish > start:
                val += finish-start
                start = finish
                
            ans.append(val)
            sort.add((prevstart, start))
            
        return ans
            
                
            