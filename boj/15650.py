import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def go(index, length, cur): 
    if length == m: 
        print(' '.join(cur))
        return

    if index > n: 
        return
    
    go(index, length+1, cur+str(index))
    go(index+1, length, cur)

go(1, 0, "")