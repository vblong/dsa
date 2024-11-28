from typing import List



def heapify_down(arr: List[int], n: int, index: int):
    while True:
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and arr[left] < arr[smallest]:
            smallest = left
        
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest != index:
            arr[index], arr[smallest] = arr[smallest], arr[index]
            index = smallest
        else:
            break

def heapify_up(arr: List[int], index: int):
    while index > 0:
        parent = (index - 1) // 2
        if arr[parent] > arr[index]:
            arr[parent], arr[index] = arr[index], arr[parent]
            index = parent
        else:
            break

def heapify(arr: List[int]):
    n = len(arr)
    for i in range(n // 2 -1, -1, -1):
        heapify_down(arr, n, i)

def heappush(arr: List[int], x: int):
    arr.append(x)
    heapify_up(arr, len(arr) - 1)

def heappop(arr: List[int]):
    if len(arr) == 0:
        raise IndexError("pop from an empty heap")
    
    arr[0], arr[-1] = arr[-1], arr[0]

    popped_value = arr.pop()

    heapify_down(arr, len(arr), 0)
    return popped_value

def heapsort(arr: List[int]):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify_down(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_down(arr, i, 0)

arr = [6, 15, 5, 9, 13, 4]
arr = [1, 2, 3]
# print('before', arr)
# heapify(arr)
# print('after', arr)
# heappush(arr, 3)
# print('push 3', arr)
# print('pop 15', heappop(arr), arr)
# heapsort(arr)
# print('heapsort', arr)
heap = []
k = 1
for n in arr:
    heappush(heap, n)
    print('push', n, heap)
    if len(heap) > k:
        heappop(heap)
        print('after pop', heap)
    else:
        print('-- no pop')