'''나이트의 이동'''
import sys
from collections import deque
input = sys.stdin.readline

dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]

t = int(input())
for _ in range(t): 
    n = int(input())
    sr, sc = map(int, input().split())
    gr, gc = map(int, input().split())
    visited = [[-1] * n for _ in range(n)]
    
    q = deque([(sr, sc)])
    visited[sr][sc] = 0 
    while q: 
        r, c = q.popleft()
        for i in range(len(dr)): 
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == -1: 
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

    print(visited[gr][gc])