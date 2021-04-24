import sys
from collections import deque
input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n = int(input())
a = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
answer = []

def bfs(x, y, count):
    q = deque([(x, y)])
    visited[x][y] = count
    house = 1
    
    while q: 
        r, c = q.popleft()
        for i in range(len(dr)):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and a[nr][nc] == 1 and visited[nr][nc] == 0 : 
                visited[nr][nc] = count
                q.append((nr, nc))
                house += 1
    
    answer.append(house)

count = 0
for i in range(n): 
    for j in range(n): 
        if a[i][j] == 1 and visited[i][j] == 0: 
            count += 1
            bfs(i, j, count)

print(count)
for c in sorted(answer): 
    print(c)