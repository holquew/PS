'''RGB거리'''
import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

dp = [[None for _ in range(3)] for __ in range(n)]
dp[0] = a[0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1] + a[i][0], dp[i-1][2] + a[i][0])
    dp[i][1] = min(dp[i-1][0] + a[i][1], dp[i-1][2] + a[i][1])
    dp[i][2] = min(dp[i-1][0] + a[i][2], dp[i-1][1] + a[i][2])

print(min(dp[n-1]))
