'''최단 경로'''
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
k = int(input())
adj = [[] for _ in range(v+1)]

for i in range(1, e+1): 
    s, e, w = map(int, input().split())
    adj[s].append((e, w))

min_heap = []
heapq.heappush(min_heap, (0, k))
distance = [INF] * (v+1)
distance[k] = 0

while min_heap: 
    current_weight, current_node = heapq.heappop(min_heap)
    if distance[current_node] < current_weight: 
        continue

    for node, weight in adj[current_node]:
        next_weight = current_weight + weight
        if next_weight < distance[node]: 
            distance[node] = next_weight
            heapq.heappush(min_heap, (next_weight, node))

for i in range(1, v+1): 
    if distance[i] == INF: 
        print('INF')
    else: 
        print(distance[i])

