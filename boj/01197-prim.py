import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())

edges = {}

for i in range(e):
    a, b, w = map(int, input().split())
    if a not in edges:
        edges[a] = set([(w, a, b)])
    else:
        edges[a].add((w, a, b))

    if b not in edges:
        edges[b] = set([(w, b, a)])
    else:
        edges[b].add((w, b, a))

print(edges)


def prim(start):
    mst = [start]
    check_heap = list(edges[start])
    heapq.heapify(check_heap)
    answer = 0
    # V 
    while check_heap:
        # logV
        w, n1, n2 = heapq.heappop(check_heap)
        if n2 not in mst:
            mst.append(n2)
            answer += w
            # 2E 
            for edge in edges[n2]:
                if edge[2] not in mst:
                    # logV
                    heapq.heappush(check_heap, edge)
    
    # O(VlogV + 2ElogV = ElogV)
    return answer


print(prim(1))
