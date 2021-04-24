'''알고스팟'''
import sys
from collections import deque
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

m, n = map(int, input().split())
a = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

q = deque([(0, 0)])
visited[0][0] = True
dist[0][0] = 0
while q: 
    r, c = q.popleft()
    for i in range(len(dr)): 
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]: 
            visited[nr][nc] = True
            if a[nr][nc] == 0: 
                q.appendleft((nr, nc))
                dist[nr][nc] = dist[r][c]
            elif a[nr][nc] == 1: 
                q.append((nr, nc))
                dist[nr][nc] = dist[r][c] + 1

print(dist[n-1][m-1])
        