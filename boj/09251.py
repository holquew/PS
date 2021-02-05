import sys
from collections import deque
input = sys.stdin.readline

a = deque(input().rstrip())
b = deque(input().rstrip())
a.appendleft('0')
b.appendleft('0')

len_a = len(a)
len_b = len(b)

dp = [[0 for _ in range(len_a)] for __ in range(len_b)]

for i in range(1, len_b):
    for j in range(1, len_a):
        if a[j] == b[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])
