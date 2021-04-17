import sys
input = sys.stdin.readline


def go(index, first, second):
    if index == n:
        t1 = 0
        t2 = 0 
        for f in first: 
            for t in first: 
                if f == t: 
                    continue
                t1 += s[f][t]
        
        for se in second: 
            for d in second: 
                if se == d: 
                    continue
                t2 += s[se][d]
        
        diff = abs(t1-t2)
        return diff 
    
    ans = -1 
    t1 = go(index+1, first+[index], second)
    if ans == -1 or (t1 != -1 and ans > t1): 
        ans = t1
    t2 = go(index+1, first, second+[index])
    if ans == -1 or (t2 != -1 and ans > t2): 
        ans = t2
    
    return ans
     

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

print(go(0, [], []))
