#https://leetcode.com/problems/find-median-from-data-stream/
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap,-num)

        if self.min_heap and self.max_heap and (-self.min_heap[0] > self.max_heap[0]):
            val = -heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,val)

        if len(self.min_heap)>len(self.max_heap)+1 :
            val = -heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,val)

        if len(self.max_heap)>len(self.min_heap):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,val)





    def findMedian(self) -> float:
       
        if len(self.min_heap) > len(self.max_heap):
            return -self.min_heap[0]

        else:
            return (-self.min_heap[0] + self.max_heap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
