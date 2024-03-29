import heapq
import sys
input = sys.stdin.readline


n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap):
            print(heap[0][1])
            heapq.heappop(heap)
        else:
            print('0')
    else:
        heapq.heappush(heap, (-num, num))
