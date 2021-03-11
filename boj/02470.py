'''두 용액'''
import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]
a.sort()

i = 0
j = n-1
answer = (a[i], a[j])
temp_min = a[i] + a[j]
while True:
    if i >= j:
        break
    
    s = a[i] + a[j]
    if abs(s) < abs(temp_min): 
        temp_min = s
        answer = (a[i], a[j])

    if s < 0:
        i += 1
    else: 
        j-= 1

print(*answer)


# 5
# -5, -4, -3, -2, -1

# 답: -1 -2
