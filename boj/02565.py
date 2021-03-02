'''전깃줄'''
import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

dp = [1] * n
a.sort(key=lambda x: x[0])
for i in range(n): 
    for j in range(i, n): 
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]: 
            dp[j] = max(dp[j], dp[i] + 1)

print(n - max(dp))


