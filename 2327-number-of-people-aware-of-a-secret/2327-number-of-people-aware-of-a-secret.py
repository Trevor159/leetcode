class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        queue = deque([0 for _ in range(forget)])
        
        queue[-1] = 1
        # print(queue)
        
        for day in range(n-1):
                
            queue.popleft()
            new = 0
            for i in range(forget-delay):
                if i >= len(queue):
                    break
                    
                new += queue[i]
            
            queue.append(new)
            
            # print((day+1), queue)
        
        
        
        
        return sum(queue) % (10 ** 9 + 7)