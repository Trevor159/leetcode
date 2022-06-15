class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        wordSet = set(words)
        
        @cache
        def findLongestString(word):
            N = len(word)
            longestChild = 0
            for i in range(N):
                newWord = word[:i] + word[i+1:]
                if newWord in wordSet:
                    longestChild = max(longestChild, findLongestString(newWord))
                    
            return longestChild + 1
        
        ans = 0
        for word in wordSet:
            ans = max(ans, findLongestString(word))
            
        return ans
        
        
        
        