class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        N1 = len(s1)
        N2 = len(s2)
        N3 = len(s3)
        
        if N1 + N2 != N3:
            return False
        
        @cache
        def helper(index1, index2):
            
            if index1 == N1 and index2 == N2:
                return True
            
            ret = False
            
            if index1 < N1 and s1[index1] == s3[index1 + index2]:
                ret |= helper(index1+1, index2)
                
            if index2 < N2 and s2[index2] == s3[index1 + index2]:
                ret |= helper(index1, index2+1)
                
            return ret
        
        return helper(0,0)
            
            
            
            