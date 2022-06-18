class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        convertedString = []
        
        prev = None
        count = 0
        for c in s:
            if c != prev:
                if prev:
                    convertedString.append((prev, count))
                    
                prev = c
                count = 0
            
            count += 1
            
        convertedString.append((prev, count))
        
        
        ans = 0
        N = len(convertedString)
        for word in words:
            prev = None
            count = 0
            index = -1
            
            for c in word:
                if c != prev:
                    if prev:
                        sCount = convertedString[index][1]
                        if (sCount < 3 and sCount != count) or (count > sCount):
                            break
                            
                    index += 1
                    prev = c
                    count = 0
                    
                    if index == N or c != convertedString[index][0]:
                        break
                    
                sCount = convertedString[index][1]
                count += 1
                
                if count > sCount:
                    break
            
            
            if index == N-1 and prev == convertedString[index][0]:
                sCount = convertedString[index][1]
                if (sCount < 3 and sCount != count) or (count > sCount):
                    continue
                
                ans += 1
                
        return ans
            
        
        