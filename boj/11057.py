import sys
input = sys.stdin.readline

n = int(input())

dp = [[1 for __ in range(10)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1]) % 10007

print(dp[n][-1])
