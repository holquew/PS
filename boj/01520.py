'''내리막길'''
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


dp = []
visited = []


# sx, sy 위치에서 n-1, m-1 갈 수 있는 경로의 수 를 리턴 중 
def dfs(graph, sx, sy):
    # 갈수 있어! sx, sy 위치 dp에 1 더해!
    if sx == n - 1 and sy == m - 1:
        return 1

    # 이미 방문해봤나봐 sx, sy 위치 dp값을 그냥 리턴해. 이미 끝까지 갈 수 있는지 확인해 봤을 거야
    if visited[sy][sx]:
        return dp[sy][sx]

    visited[sy][sx] = True
    dp[sy][sx] = 0
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] < graph[sy][sx]:
            # 각 위치로 부터 dfs를 다시 시작해서 도착지까지 갈 수 있는 경로를 구해 오기
            dp[sy][sx] += dfs(graph, nx, ny)

    return dp[sy][sx]


m, n = map(int, input().split())
graph = []
dp = [[0 for col in range(n)] for row in range(m)]
visited = [[False for col in range(n)] for row in range(m)]
for i in range(m):
    graph.append(list(map(int, input().split())))

print(dfs(graph, 0, 0))
for i in dp:
    print(i)

for i in graph:
    print(i)
