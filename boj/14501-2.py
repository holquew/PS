import sys
input = sys.stdin.readline

def go(now, profit, n, take, pay): 
    global ans
    
    if now > n: 
        return
    
    if now == n: 
        if ans < profit: 
            ans = profit
        return
    
    go(now+take[now], profit+pay[now], n, take, pay)
    go(now+1, profit, n, take, pay)
    


n = int(input())
t = []
p = []
for _ in range(n): 
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

ans = 0
go(0, 0, n, t, p)
print(ans)