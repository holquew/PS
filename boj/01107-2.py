'''리모컨'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
if m > 0: 
    broken = set(map(int, input().split()))
else: 
    broken = []

MAX = 1000001
# 일단 다 만들자 

answer = abs(100 - n)
for ch in range(MAX):
    num_set = set(map(int, list(str(ch))))
    if len(broken.intersection(num_set)) == 0: 
        temp = abs(n - ch) + len(list(str(ch)))
        if answer > temp: 
            answer = temp

print(answer)

    
