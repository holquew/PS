'''내리막길'''
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

visited = [[False] * n for _ in range(m)]
dp = [[0] * n for _ in range(m)]

def dfs(sr, sc): 
    if sr == (m-1) and sc == (n-1): 
        return 1
    if visited[sr][sc]: 
        return dp[sr][sc]
    
    visited[sr][sc] = True
    for i in range(len(dr)): 
        nr, nc = sr + dr[i], sc + dc[i]
        if 0 <= nr < m and 0 <= nc < n and a[nr][nc] < a[sr][sc]: 
            dp[sr][sc] += dfs(nr, nc)
    
    return dp[sr][sc]

print(dfs(0, 0))