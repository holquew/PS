import sys
sys.setrecursionlimit = 10**6

def dfs(node, visited, graph, weights):
    global count
    
    if visited[node]: 
        return weights[node]

    visited[node] = True
    for n in graph[node]:
        if not visited[n]:
            weights[node] += dfs(n, visited, graph, weights)
    
    weight = weights[node]
    count += abs(weight)
    
    return weight

count = 0
    
def solution(a, edges):
    global count

    graph = {}
    for x, y in edges: 
        if x not in graph: 
            graph[x] = [y]
        else: 
            graph[x].append(y)
        if y not in graph: 
            graph[y] = [x]
        else: 
            graph[y].append(x)
    
    weights = list(a)
    visited = [False] * len(a)
    
    dfs(0, visited, graph, weights)
    return count if weights[0] == 0 else -1


print(
solution(
    [-5,0,2,1,2], 
    [[0,1],[3,4],[2,3],[0,3]]
)
)