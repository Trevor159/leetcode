class Solution:
    def minDeletions(self, s: str) -> int:
        counts = [0] * 26
        
        for c in s:
            counts[ord(c) - ord("a")] += 1
            
        counts.sort(reverse=True)
        
        prev = float("inf")
        ans = 0
        amount = 0
        # print(counts)
        for i in range(26):
            num = counts[i]
            nextNum = counts[i+1] if i != 25 else 0
            
            if num < prev:
                prev = num
                continue
                
            amount += 1
            
            while amount and prev > nextNum:
                ans += amount
                prev -= 1
                amount -= 1
                
                
        return ans
        
        
        
        