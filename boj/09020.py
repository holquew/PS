import sys
import math
input = sys.stdin.readline

n = 10001
m = int(math.sqrt(n)) + 1
isPrime = [True] * n

for i in range(2, m):
    if isPrime[i] == True:
        for j in range(2*i, n, i):
            isPrime[j] = False

primes = [i for i in range(1, n) if isPrime[i] == True]


def get_partition(a):
    start = max([i for i in range(len(primes)) if primes[i] <= a//2])
    for i in range(start, 0, -1):
        for j in range(i, len(primes)):
            if primes[i] + primes[j] == a:
                return (primes[i], primes[j])


t = int(input())
for _ in range(t):
    a = int(input())
    answers = get_partition(a)
    print(f'{answers[0]} {answers[1]}')
