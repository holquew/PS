import sys
input = sys.stdin.readline

n = int(input())
t = [0]
p = [0]
for _ in range(n): 
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

ans = -987654321
def go(day, pay):
    global ans 

    if day == n+1: 
        ans = max(ans, pay) 

    if day > n: 
        return 
    
    go(day+t[day], pay+p[day])
    go(day+1, pay)

go(1, 0)
print(ans)

    