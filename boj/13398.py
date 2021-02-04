'''연속합 2'''
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))


dp = [[i for i in a] for __ in range(2)]

answer = a[0]
for i in range(1, n):
    dp[0][i] = max(dp[0][i], dp[0][i-1] + a[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + a[i])
    answer = max(answer, dp[0][i], dp[1][i])

print(dp)
