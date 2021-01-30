t = int(input())

for i in range(t):
    n = int(input())

    dp0 = [None] * 50
    dp1 = [None] * 50
    # dp0[0] = 1
    # dp0[1] = 0
    dp0[0:2] = [1, 0]
    # dp1[0] = 0
    # dp1[1] = 1
    dp1[0:2] = [0, 1]

    for j in range(2, n+1):
        dp0[j] = dp0[j-1] + dp0[j-2]
        dp1[j] = dp1[j-1] + dp1[j-2]

    print(' '.join(map(str, [dp0[n], dp1[n]])))
