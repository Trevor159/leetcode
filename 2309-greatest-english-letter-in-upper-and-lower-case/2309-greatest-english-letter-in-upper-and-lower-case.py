class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set()
        ans = ""
        for c in s:
            seen.add(c)
            
            if c.upper() in seen and c.lower() in seen:
                ans = max(ans, c.upper())
                
        return ans