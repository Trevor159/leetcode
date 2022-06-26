class StockPrice:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.mincorrections = defaultdict(int)
        self.maxcorrections = defaultdict(int)
        self.latestTimestamp = -1
        self.prices = {}
        

    def update(self, timestamp: int, price: int) -> None:
        self.latestTimestamp = max(self.latestTimestamp, timestamp)
        
        if timestamp in self.prices:
            self.mincorrections[self.prices[timestamp]] += 1
            self.maxcorrections[self.prices[timestamp]] += 1
            
        self.prices[timestamp] = price
        heappush(self.minheap, price)
        heappush(self.maxheap, -price)
        
        while self.mincorrections[self.minheap[0]] > 0:
            self.mincorrections[self.minheap[0]] -= 1
            heappop(self.minheap)
            
        while self.maxcorrections[-self.maxheap[0]] > 0:
            self.maxcorrections[-self.maxheap[0]] -= 1
            heappop(self.maxheap)

    def current(self) -> int:
        return self.prices[self.latestTimestamp]

    def maximum(self) -> int:
        return -self.maxheap[0]

    def minimum(self) -> int:
        return self.minheap[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()