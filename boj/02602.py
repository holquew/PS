'''돌다리 건너기'''
import sys
input = sys.stdin.readline

order = list(input().rstrip())
bridge = [list(input().rstrip()) for _ in range(2)]

n = len(bridge[0])
m = len(order)

dp = [[[0 for _ in range(n)] for _ in range(2)] for _ in range(m)]

dp[0][0][0] = 1 if bridge[0][0] == order[0] else 0
dp[0][1][0] = 1 if bridge[1][0] == order[0] else 0

for side in range(2):
    for step in range(1, n):
        dp[0][side][step] = dp[0][side][step-1]
        if bridge[side][step] == order[0]:
            dp[0][side][step] += 1


for i in range(1, m):
    for side in range(2):
        for step in range(1, n):
            dp[i][side][step] = dp[i][side][step-1]
            if bridge[side][step] == order[i]:
                dp[i][side][step] += dp[i-1][(side+1) % 2][step-1]


count = dp[-1][0][-1] + dp[-1][1][-1]
print(count)
