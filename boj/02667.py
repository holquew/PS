import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

visited = [[0 for _ in range(n)] for __ in range(n)]

house_counts = []
section_count = 1


def bfs(x, y, count):
    q = deque([(x, y)])
    visited[x][y] = count
    house = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if a[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = count
                house += 1

    house_counts.append(house)


count = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and visited[i][j] == 0:
            count += 1
            bfs(i, j, count)

print(count)
for i in sorted(house_counts):
    print(i)
