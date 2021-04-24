'''이분 그래프'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
t = int(input())
for _ in range(t): 
    node, edge = map(int, input().split())
    graph = [[] for _ in range(node+1)]
    color = [0] * (node+1)
    for _ in range(edge): 
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, c): 
        color[node] = c
        for n in graph[node]: 
            if color[n] == 0: 
                if not dfs(n, 3-c): 
                    return False
            elif color[node] == color[n]: 
                return False
        
        return True

    ok = True
    for i in range(1, node + 1):
        if color[i] == 0: 
            if not dfs(i, 1): 
                ok = False
                    
        
    print('YES' if ok else 'NO')

import sys
sys.setrecursionlimit(1000000)
t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    a = [[] for _ in range(n)]
    color = [0] * n
    for _ in range(m):
        u,v = map(int,sys.stdin.readline().split())
        a[u-1].append(v-1)
        a[v-1].append(u-1)
    
    def dfs(x, c):
        color[x] = c
        for y in a[x]:
            if color[y] == 0:
                if not dfs(y, 3-c):
                    return False
            elif color[y] == color[x]:
                return False
        return True
    
    ans = True
    for i in range(n):
        if color[i] == 0:
            if not dfs(i, 1):
                ans = False
    
    print('YES' if ans else 'NO')