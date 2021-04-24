import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

node, edge = map(int, input().split())
graph = [[] for _ in range(node+1)]
for _ in range(edge): 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

visited = [False for _ in range(node+1)]
def dfs(s):
    visited[s] = True
    for n in graph[s]: 
        if not visited[n]: 
            dfs(n)

answer = 0
for i in range(1, node+1): 
    if not visited[i]: 
        dfs(i)
        answer += 1

print(answer)