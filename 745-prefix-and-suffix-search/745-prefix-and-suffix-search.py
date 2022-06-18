class Trie:
    def __init__(self):
        self.data = [None] * 26
        self.words = set()

class WordFilter:

    def __init__(self, words: List[str]):
        self.prefixes = Trie()
        self.indexes = {}
        
        
        for i in range(len(words)):
            word = words[i]
            self.indexes[word] = i
        
        for word in words:
            trie = self.prefixes
            for c in word:
                char = ord(c) - ord("a")
                if not trie.data[char]:
                    trie.data[char] = Trie()
                    
                trie = trie.data[char]
                trie.words.add(word)
                
                
        self.suffixes = Trie()
        for word in words:
            trie = self.suffixes
            for c in reversed(word):
                char = ord(c) - ord("a")
                if not trie.data[char]:
                    trie.data[char] = Trie()
                    
                trie = trie.data[char]
                trie.words.add(word)
            
            

    def f(self, prefix: str, suffix: str) -> int:
        trie = self.prefixes
        
        for c in prefix:
            char = ord(c) - ord("a")
            
            if not trie.data[char]:
                return -1
            
            trie = trie.data[char]
            
        words = trie.words
        # print(words)
        trie = self.suffixes
        
        for c in reversed(suffix):
            char = ord(c) - ord("a")
            
            if not trie.data[char]:
                return -1
            
            trie = trie.data[char]
            
        # print(trie.words)
        words = words & trie.words
        # print(words)
        
        ans = -1
        for word in words:
            ans = max(ans, self.indexes[word])
            
        # print(ans)
        return ans
            
            
            


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)