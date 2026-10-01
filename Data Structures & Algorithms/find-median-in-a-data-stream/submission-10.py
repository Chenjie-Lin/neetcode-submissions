class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= self.maxHeap[0]:
            heapq.heappush_max(self.maxHeap, num)
        elif not self.minHeap or num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush_max(self.maxHeap, num)

        if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            
            if len(self.maxHeap) > len(self.minHeap):
                heapq.heappush(self.minHeap, heapq.heappop_max(self.maxHeap))
            else:
                heapq.heappush_max(self.maxHeap, heapq.heappop(self.minHeap))
        

    def findMedian(self) -> float:
        if ((len(self.maxHeap) + len(self.minHeap)) % 2) == 1:
            return self.maxHeap[0] if len(self.maxHeap) > len(self.minHeap) else self.minHeap[0]
        else:
            return (self.maxHeap[0] + self.minHeap[0]) / 2
        