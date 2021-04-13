import sys
input = sys.stdin.readline

MAX = 1000000

n = int(input())
m = int(input())
if m > 0: 
    a = list(map(int, input().split()))
else: 
    a = []

ans = abs(n - 100)

for channel in range(0, MAX):
    b = set(map(int, list(str(channel))))
    if len(list(set(a).intersection(b))) == 0:
        temp = abs(channel - n) + len(list(str(channel)))
        if temp < ans: 
            ans = temp

print(ans)
