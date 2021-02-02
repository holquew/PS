import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i+1, n):
        if a[i] < a[j]:
            dp[j] = max(dp[j], dp[i] + 1)

max_dp = max(dp)
print(max_dp)

answer = deque([])
for k in range(n-1, -1, -1):
    if dp[k] == max_dp:
        answer.appendleft(a[k])
        max_dp -= 1

print(' '.join(map(str, answer)))
