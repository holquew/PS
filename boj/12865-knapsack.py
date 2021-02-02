import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

weights = [0]
values = [0]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split())
    weights.append(w)
    values.append(v)

dp = [[0 for _ in range(k + 1)] for __ in range(n+1)]
for i in range(n + 1):
    for w in range(k+1):
        if i == 0 or w == 0:
            dp[i][w] = 0
        elif weights[i] <= w:
            dp[i][w] = max(values[i] + dp[i-1][w-weights[i]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[n][k])
