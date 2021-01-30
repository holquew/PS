import heapq

n, k = map(int, input().split())
nums = list(map(int, input().split()))

heap = []
for i in nums:
    heapq.heappush(heap, i)

# heapq.heapify(nums)

for _ in range(k - 1):
    heapq.heappop(heap)

print(heapq.heappop(heap))
