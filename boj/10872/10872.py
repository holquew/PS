import sys
sys.setrecursionlimit(20000)
n = int(input())

memo = [None] * 10001
memo[0] = 0
memo[1] = 1


def fib(a):
    if memo[a] == None:
        memo[a] = fib(a-1) + fib(a-2)

    return memo[a]


print(fib(n))
