# dfs와 bfs
from collections import deque
n, m, v = map(int, input().split())

visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


# def dfs(node, visited):
#     visited[node] = True
#     print(node, end=' ')
#     for i in graph[node]:
#         if not visited[i]:
#             dfs(i, visited)

def dfs(start, visited):
    stack = [start]

    while stack:
        node = stack.pop()
        if visited[node]:
            continue

        visited[node] = True
        print(node, end=' ')

        for i in reversed(graph[node]):
            stack.append(i)


def bfs(start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        n = queue.popleft()
        print(n, end=' ')
        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(v, visited1)
print()
bfs(v, visited2)
