class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        UF = {}
        
        def find(x):
            if x == UF[x]:
                return x
            return find(UF[x])
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            
            UF[find(x)] = find(y)
            
        seen = set()
        N = len(stones)
        
        for i in range(N):
            x, y = stones[i]
            union(x, ~y)
            
        for i in range(N):
            x, y = stones[i]
            seen.add(find(x))
            
        return N-len(seen)
                
                
                
                
                
                
                
                
        
        
        
        