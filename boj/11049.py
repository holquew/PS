'''행렬 곱셈 순서'''
n = int(input())
m = []
for _ in range(n):
    a, b = map(int, input().split())
    m.append((a, b))

dp = [[0 for _ in range(n)] for _ in range(n)]

for k in range(0, n):
    for i in range(0, n):
        j = k + i
        if j >= n or i == j:
            continue

        dp[i][j] = float('inf')
        for a in range(i, j):
            dp[i][j] = min(dp[i][j],
                           dp[i][a] + dp[a+1][j] + m[i][0] * m[a][1] * m[j][1])

print(dp[0][n-1])
