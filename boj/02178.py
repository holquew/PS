import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
a = [list(map(int, input().rstrip())) for y in range(n)]


def bfs(sy, sx):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque([(sy, sx)])
    visited[sy][sx] = 1

    while queue:
        y, x = queue.popleft()
        if y == n-1 and x == m-1:
            print(visited[y][x])
            break

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and a[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))


bfs(0, 0)
