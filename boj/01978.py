import sys
import math
input = sys.stdin.readline

n = 1001
m = int(math.sqrt(n)) + 1
isPrime = [True] * n
isPrime[0] = False
isPrime[1] = False

for i in range(2, m):
    if isPrime[i] == True:
        for j in range(2*i, n, i):
            isPrime[j] = False

num = int(input())
a = list(map(int, input().split()))
count = 0
for check in a: 
    if isPrime[check] == True: 
        count += 1

print(count)