import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

for num in sorted(a): 
    print(num)