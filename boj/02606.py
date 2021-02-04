import sys
input = sys.stdin.readline

n = int(input())
e = int(input())

adj = [[0 for _ in range(n+1)] for __ in range(n+1)]
for i in range(e):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

visited = [False] * (n+1)


def dfs(start):
    count = 0
    stk = [start]
    while stk:
        node = stk.pop()
        if visited[node]:
            continue

        count += 1
        visited[node] = True
        for i in range(1, n+1):
            if adj[node][i] == 1:
                stk.append(i)

    return count


print(dfs(1) - 1)
