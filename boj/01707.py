import sys
from collections import deque
input = sys.stdin.readline


def bfs(root):
    visited = []
    queue = deque([root])

    colored[root] = 1
    while queue:
        n = queue.popleft()
        current_color = colored[n]
        for node in graph[n]:
            if colored[node] == 0:
                colored[node] = -current_color
                queue.append(node)
            elif colored[node] == colored[n]:
                return False

    return True


t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    graph = {}
    colored = [0 for _ in range(v + 1)]
    for __ in range(e):
        a, b = map(int, input().split())
        if a not in graph:
            graph[a] = [b]
        elif b not in graph[a]:
            graph[a].append(b)

        if b not in graph:
            graph[b] = [a]
        elif a not in graph[b]:
            graph[b].append(a)

    for i in range(1, v+1):
        if colored[i] == 0:
            if bfs(i) == False:
                print("NO")
                break
    else:
        print("YES")

