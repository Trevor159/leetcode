class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:

        if num == 0:
            return 0
        
        numOnes = num % 10
        
        for i in range(1, 11):
            val = k * i
            if val > num:
                return -1
            
            kOnes = val % 10
            
            if kOnes == numOnes:
                return i
            
            
        return -1