import sys
input = sys.stdin.readline

def go(n, s): 
    if s == n: 
        return 1
    if s > n: 
        return 0
    
    ret = 0
    for i in range(1, 4): 
        ret += go(n, s+i)
    
    return ret
    


t = int(input())
for _ in range(t): 
    n = int(input())
    print(go(n, 0))
