import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# used = [False for _ in range(n+1)]

def go(index, cur): 
    if index == m:
        print(' '.join(cur))
        return
        
    for i in range(1, n+1): 
        # if used[i]: 
        #     continue
        # used[i] = True
        go(index+1, cur+str(i))
        # used[i] = False


go(0, "")
