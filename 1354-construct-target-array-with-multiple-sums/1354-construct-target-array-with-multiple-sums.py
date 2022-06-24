class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        N = len(target)
        total = sum(target)
        
        if N == 1:
            return target[0] == 1
        
        for i in range(N):
            target[i] = -target[i]
            
        heapify(target)
        
        while target and -target[0] != 1:
            # print(target)
            maximum = -heappop(target)
            total -= maximum
            if total == 1:
                return True
            
            val = (maximum % total)
            # print(val)
            # print(maximum)
            
            if val <= 0 or val == maximum:
                return False
            total += val
            
            heappush(target, -val)
            
        return True