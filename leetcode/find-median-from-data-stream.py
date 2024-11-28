from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        self.heap = []
        self.currentMedian = 0
        self.arr = []
        self.shift = 0

    def addNum(self, num: int) -> None:
        # heappush(self.heap, num)
        self.arr.append(num)
        self.arr = sorted(self.arr)

    def findMedian(self) -> float:
        # print('find median, current arr', self.arr)
        # k1 = len(self.arr) // 2
        # k2 = 0
        # if len(self.arr) % 2 == 0:
        #     k2 = k1 + 1
            
        # k = k1
        # if len(self.arr) % 2 == 0:
        #     k = k2
        # else:
        #     k += 1
        # print('k1=', k1, ', k2=', k2)
        # heap = []
        # for n in self.arr:
        #     heappush(heap, n)
        #     if len(heap) > k:
        #         heappop(heap)
        # print('heap is', heap)
        # if len(self.arr) % 2 == 0:
        #     print('-----returning', f'({heap[0]}+{heap[1]})/2', (heap[0] + heap[1]) / 2)
        #     return (heap[0] + heap[1]) / 2
        # print('-----returning', heap[0])
        # return heap[0]
        n = len(self.arr)
        if n % 2 == 0:
            return (self.arr[n // 2] + self.arr[n // 2 - 1]) / 2
        return self.arr[n // 2]

            

obj = MedianFinder()
# obj.addNum(1)    # arr = [1]
# obj.addNum(2)    # arr = [1, 2]
# obj.findMedian() # return 1.5 (i.e., (1 + 2) / 2)
# obj.addNum(3)    # arr[1, 2, 3]
# obj.findMedian() # return 2.0

obj.addNum(-1)
print(obj.findMedian()) # -1
obj.addNum(-2) 
print(obj.findMedian()) # -1.5
obj.addNum(-3)
print(obj.findMedian()) # -2
obj.addNum(-4)
print(obj.findMedian()) # -2.5
obj.addNum(-5)
print(obj.findMedian()) # -3