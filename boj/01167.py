'''트리의 지름'''
import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

v = int(input())
tree = defaultdict(list)
dp = [None for _ in range(v+1)]
visited1 = [False for _ in range(v+1)]
visited2 = [False for _ in range(v+1)]

for i in range(1, v+1):
    a = list(map(int, input().split()))
    for j in range(1, len(a)-1, 2):
        tree[a[0]].append((a[j], a[j+1]))

# print(tree)


def bfs(start, visited):
    node, dist = 0, 0
    queue = deque([(start, 0)])

    visited[start] = True
    while queue:
        now, dist_now = queue.popleft()
        for n in tree[now]:
            if not visited[n[0]]:
                visited[n[0]] = True
                queue.append((n[0], n[1] + dist_now))

                if n[1] + dist_now > dist:
                    node = n[0]
                    dist = n[1] + dist_now

    return node, dist


temp, temp_dist = bfs(1, visited1)
print(bfs(temp, visited2)[1])
