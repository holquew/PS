import sys
input = sys.stdin.readline

n = int(input())
t = [0 for _ in range(n+2)]
p = [0 for _ in range(n+2)]
for i in range(1, n+1):
    a, b = map(int, input().split())
    t[i], p[i] = a, b

dp = [0 for _ in range(n+2)]
for i in range(n, 0, -1):
    if (i + t[i]) <= (n + 1):
        dp[i] = max(dp[i+1], dp[i+t[i]] + p[i])
    else:
        dp[i] = dp[i+1]


print(dp[1])
