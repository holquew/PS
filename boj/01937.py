import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
field = [[int(x) for x in input().split()] for y in range(n)]

dp = [[0 for _ in range(n)] for __ in range(n)]


def dfs(x, y):
    if dp[y][x] != 0:
        return dp[y][x]

    dp[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and field[ny][nx] > field[y][x]:
            dp[y][x] = max(dp[y][x], dfs(nx, ny) + 1)

    return dp[y][x]


answer = 0
for i in range(n):
    for j in range(n):
        dfs(i, j)


print(max(map(max, dp)))
