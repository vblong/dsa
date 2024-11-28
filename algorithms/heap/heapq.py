
from heapq import heapify, heappop, heappush


arr = [6, 15, 5, 9, 13, 4]

minHeap = []
heappush(minHeap, 2)
heappush(minHeap, 1)
heappush(minHeap, 4)
print(minHeap)
heapify(arr)
print(arr)
heappush(arr, 3)
print(arr)
heappop(arr)
print(arr)