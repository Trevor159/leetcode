class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            
        seen = set()
        childrenMap = {}
        xors = {}
        
        def processNode(node):
            val = nums[node]
            children = set()
            seen.add(node)
            for child in graph[node]:
                if child in seen:
                    continue
                    
                nodeVal, nodeChilds = processNode(child)
                children.add(child)
                children |= nodeChilds
                val ^= nodeVal
                
            childrenMap[node] = children
            xors[node] = val
            
            return (val, children)
        
        
            
        processNode(0)
        # print(xors)
        # print(childrenMap)
        
        N = len(edges)
        ans = float("inf")
        for i in range(N):
            for j in range(i+1, N):
                a, b = edges[i]
                c, d = edges[j]
                
                child1 = b if b in childrenMap[a] else a
                child2 = d if d in childrenMap[c] else c
                
                if child1 in childrenMap[child2]:
                    val1 = xors[child1]
                    val2 = xors[child2] ^ val1
                    val3 = xors[0] ^ xors[child2]
                    
                elif child2 in childrenMap[child1]:
                    val1 = xors[child2]
                    val2 = xors[child1] ^ val1
                    val3 = xors[0] ^ xors[child1]
                else:
                    val1 = xors[child1]
                    val2 = xors[child2]
                    val3 = xors[0] ^ val2 ^ val1
                    
                ans = min(ans, max(val1, val2, val3) - min(val1, val2, val3))
                
        return ans
                
        
        