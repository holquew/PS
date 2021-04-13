import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

def p(x):
    count = 0 
    for i in range(1, n+1): 
        count += min(n, x//i)
    return count

start = 1
end = k

answer = -1
while start <= end:
    mid = (start + end) // 2
    c = p(mid)
    if c >= k: 
        answer = mid
        end = mid - 1
    else: 
        start = mid + 1

print(answer)