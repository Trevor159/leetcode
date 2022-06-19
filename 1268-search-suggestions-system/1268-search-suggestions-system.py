class Trie:
    def __init__(self):
        self.data = [None]*26
        self.list = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        
        products.sort()
        base = Trie()
        for word in products:
            trie = base
            
            for c in word:
                charVal = ord(c) - ord("a")
                if not trie.data[charVal]:
                    trie.data[charVal] = Trie()
                    
                trie = trie.data[charVal]
                
                if len(trie.list) < 3:
                    trie.list.append(word)
                    
        trie = base
        for c in searchWord:
            charVal = ord(c) - ord("a")
            
            if trie:
                trie = trie.data[charVal]
                
            if trie:
                ans.append(trie.list)
            else:
                ans.append([])
                
        return ans