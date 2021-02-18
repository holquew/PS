import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

m, n = map(int, input().split())
a = [[None for _ in range(m)] for _ in range(n)]
start = []
zeros = 0

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            start.append((i, j))
        elif row[j] == 0:
            zeros += 1

        a[i][j] = row[j]

if zeros == 0:
    print('0')
    exit(0)


def bfs(start, zeros):
    queue = deque([])
    for s in start:
        queue.append(s)

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and a[ny][nx] == 0:
                zeros -= 1
                a[ny][nx] = a[y][x] + 1
                queue.append((ny, nx))

    return zeros


zeros = bfs(start, zeros)
if zeros == 0:
    print(max(map(max, a)) - 1)
else:
    print('-1')
