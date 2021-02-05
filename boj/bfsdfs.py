from collections import deque


graph_list = {1: set([2, 3, 4]),
              2: set([1, 4]),
              3: set([1, 4]),
              4: set([1, 2, 3])}
root_node = 1


def bfs(graph, root):
    visited = []
    queue = deque([root])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)

    return visited


def dfs(graph, root):
    visited = []
    stack = [root]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)

    return visited


print(dfs(graph_list, root_node))
print(bfs(graph_list, root_node))
