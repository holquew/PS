import sys
input = sys.stdin.readline

use = [-1, -1, 1, 7, 4, 2, 0, 8, 10]
dp = [None for _ in range(101)]
dp[:9] = use
dp[6] = 6

for i in range(9, 101): 
    dp[i] = float('inf')
    for j in range(2, 8): 
        dp[i] = min(dp[i-j]*10 + use[j], dp[i])

t = int(input())
for _ in range(t): 
    n = int(input())
    if n == 2: 
        print('1 1')
        continue
    
    if n % 2 == 1: 
        big = '7'+'1'*(n//2-1)
    else: 
        big = '1'*(n//2)
    
    print(dp[n], big)