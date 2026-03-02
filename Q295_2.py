class MedianFinder: # 2 heaps common way, push to max first

    def __init__(self):
        #max and min heaps
        self.maxheap = [] #smaller nums
        self.minheap = [] #bigger nums
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num) #python works in min heap so to make it max I make nums negative
        
        if self.maxheap and self.minheap and (-self.maxheap[0] > self.minheap[0]): #convert the - back to normal
            val = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,val)
        
        if len(self.maxheap) > len(self.minheap)+1:
            val = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,val)
        
        if len(self.minheap) > len(self.maxheap)+1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-val)
        
    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]

        else:
            return (self.minheap[0] + (-self.maxheap[0]))/2
          


class MedianFinder: # 2 heaps with decide where to push first FASTER

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        
    def addNum(self, num: int) -> None:
        if not self.maxheap or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap,num)
        
        if len(self.maxheap) > len(self.minheap)+1:
            val = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,val)
        
        if len(self.minheap) > len(self.maxheap): # minheap can't be bigger than maxheap this time
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-val)
        
    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        return (self.minheap[0] + (-self.maxheap[0]))/2
