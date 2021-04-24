import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().rstrip())) for _ in range(n)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

visited = [[0] * m for _ in range(n)]
def bfs(sr, sc): 
    q = deque([(sr, sc)])
    count = 1
    visited[sr][sc] = count
    while q: 
        r, c = q.popleft()
        for i in range(len(dr)): 
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and a[nr][nc] == 1 and visited[nr][nc] == 0: 
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

bfs(0, 0)
print(visited[n-1][m-1])