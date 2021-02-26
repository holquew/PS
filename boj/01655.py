'''가운데를 말해요'''
import sys
import heapq
input = sys.stdin.readline

n = int(input())
max_heap = []
min_heap = []

for _ in range(n):
    new = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-new, new))
    else:
        heapq.heappush(min_heap, (new, new))

    if len(min_heap) >= 1 and min_heap[0][1] < max_heap[0][1]:
        _, to_min = heapq.heappop(max_heap)
        _, to_max = heapq.heappop(min_heap)
        heapq.heappush(min_heap, (to_min, to_min))
        heapq.heappush(max_heap, (-to_max, to_max))

    print(max_heap[0][1])
