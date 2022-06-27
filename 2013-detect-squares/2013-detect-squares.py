class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        val = 0
        for x2, y2 in self.points:
            if x1 == x2 or y1 == y2 or abs(x2-x1) != abs(y2-y1):
                continue
                
            if (x1, y2) in self.points and (x2, y1) in self.points:
                val += self.points[(x2, y2)] * self.points[(x2, y1)] * self.points[(x1, y2)]
                
        return val


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)