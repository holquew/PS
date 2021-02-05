import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(graph, a, b):
    queue = deque([(a, b)])
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0 for _ in range(n)] for __ in range(m)]
    for i in range(k):
        a, b = map(int, input().split())
        field[a][b] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                count += 1
                bfs(field, i, j)

    print(count)
