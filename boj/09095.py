# import sys
# input = sys.stdin.readline

# n = int(input())
# dp = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for _ in range(n):
#     a = int(input())
#     if a > 3:
#         for i in range(4, a+1):
#             dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

#     print(dp[a])

import sys
input = sys.stdin.readline

def go(count, s, goal): 
    if s == goal: 
        return 1
    if s > goal: 
        return 0
    
    ret = 0
    for i in range(1, 4): 
        # 1, 2, 3 을 각각 더해 보고 
        ret += go(count + 1, s + i, goal)
    
    return ret

t = int(input())
for _ in range(t):
    n = int(input())
    print(go(0, 0, n))

