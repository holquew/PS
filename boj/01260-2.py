import sys
from collections import deque
input = sys.stdin.readline

node, edge, start = map(int, input().split())
graph = {}
for _ in range(edge):
    a, b = map(int, input().split())
    if a not in graph: 
        graph[a] = [b]
    else: 
        graph[a].append(b)
    if b not in graph: 
        graph[b] = [a]
    else: 
        graph[b].append(a)

for i in graph.values(): 
    i.sort()

bfs_visited = [False for _ in range(node + 1)]
dfs_visited = [False for _ in range(node + 1)]

bfs_answer = []
dfs_answer = []

def dfs(s, graph, visited): 
    global dfs_answer

    visited[s] = True 
    dfs_answer.append(s)
    for n in graph[s]:
        if not visited[n]: 
            dfs(n, graph, visited)

def bfs(s, graph, visited): 
    global bfs_answer

    visited[s] = True 
    queue = deque([s])
    while queue: 
        pop = queue.popleft() 
        bfs_answer.append(pop)
        for n in graph[pop]: 
            if not visited[n]:
                visited[n] = True
                queue.append(n)

dfs(start, graph, dfs_visited)
bfs(start, graph, bfs_visited)
print(' '.join(map(str, dfs_answer)))
print(' '.join(map(str, bfs_answer)))
    
