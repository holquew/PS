n = int(input())

memo = [0, 1, 2]

for i in range(3, n):
    memo.append(memo[i-1] + memo[i-2])

print(memo[n] % 10007)


memo = [None] * (n+1)
memo[1] = 1
memo[2] = 2

for i in range(3, n+1):
    memo[i] = memo[i-1] + memo[i-1]

print(memo[n] % 10007)
