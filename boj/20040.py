'''사이클 게임'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = [x for x in range(n)]

def find(x): 
    if x == p[x]: 
        return x
    else: 
        p[x] = find(p[x])
        return p[x]


def union(a, b): 
    x = find(a)
    y = find(b)
    if x != y: 
        if x < y: 
            p[y] = x    
        else: 
            p[x] = y

def is_same_parent(a, b): 
    return True if find(a) == find(b) else False

answer = 0
for order in range(m): 
    a, b = map(int, input().split())
    if not is_same_parent(a, b): 
        union(a, b)
    else: 
        answer = order + 1
        print(answer)
        exit(0)

print(answer)

    
