'''파일 합치기'''
import sys
input = sys.stdin.readline
inf = 987654321

t = int(input())
for _ in range(t): 
    k = int(input())
    p = [int(x) for x in input().split()]
    dp = [[0] * k for _ in range(k)]
    psum = [[None] for _ in range(k)]

    psum = {-1:0}
    for i in range(k): 
        psum[i] = psum[i-1] + p[i]

    for m in range(1, k): 
        for i in range(k - m):
            j = i + m 
            if j - i == 1:
                dp[i][j] = p[i] + p[j] 
                continue     

            dp[i][j] = inf
            for a in range(i, j): 
                dp[i][j] = min(dp[i][j], dp[i][a] + dp[a+1][j] + psum[j] - psum[i-1])
            
    print(dp[0][-1])


