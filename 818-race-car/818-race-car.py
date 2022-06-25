class Solution:
    def racecar(self, target: int) -> int:
        
        queue = deque()
        
        queue.append((0, 0, 1))
        
        while queue:
            
            steps, position, speed = queue.popleft()
            
            if target == position:
                return steps
            
            steps += 1
            
            queue.append((steps, position + speed, speed * 2))
            
            dist = target - position
            
            posDist = dist > 0
            posSpeed = speed > 0
            
            if posDist ^ posSpeed or abs(dist) < abs(speed):
                speed = 1 if speed < 0 else -1
                
                queue.append((steps, position, speed))