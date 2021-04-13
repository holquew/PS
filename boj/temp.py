import sys
input = sys.stdin.readline

n, m = map(int, input().split())

c = [False for _ in range(10)]
a = [0 for _ in range(10)]
def go(index, start, n, m): 
    if index == m: 
        print(' '.join(map(str,a[:m])))
        return
    
    for i in range(start, n+1): 
        # if c[i]: 
        #     continue

        c[i] = True
        a[index] = i
        go(index + 1, i, n, m)
        c[i] = False

go(0, 1, n, m)