'''리모컨'''
import sys
input = sys.stdin.readline

def possible(ch, broken): 
    if ch == 0: 
        return 0 if broken[ch] else 1
    
    l = 0
    while ch > 0: 
        if broken[ch % 10]: 
            return 0

        l += 1 
        ch //= 10
    
    return l 

n = int(input())
m = int(input())
if m > 0: 
    a = list(map(int, input().split()))
else: 
    a = []

broken = [False] * 10
for i in range(m): 
    broken[a[i]] = True


MAX = 1000001
answer = abs(100 - n)
for c in range(MAX): 
    l = possible(c, broken)
    if l != 0: 
        temp = abs(n - c) + l
        if answer > temp: 
            answer = temp

print(answer)
