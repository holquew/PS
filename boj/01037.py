'''약수'''
import sys
input = sys.stdin.readline

n = int(input())
a = [x for x in map(int, input().split())]

print(min(a) * max(a))
