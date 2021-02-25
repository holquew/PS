'''트리와 쿼리'''
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, r, q = map(int, input().split())
connected = [[] for _ in range(n+1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

visited = [False for _ in range(n+1)]
count = [1 for _ in range(n+1)]


def dfs(node):
    if visited[node]:
        return count[node]

    visited[node] = True
    for n in connected[node]:
        if not visited[n]:
            count[node] += dfs(n)

    return count[node]


dfs(r)
for _ in range(q):
    c = int(input())
    print(count[c])
