import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, r, q = map(int, input().split())
connected = {}
for i in range(1, n+1):
    connected[i] = []

for _ in range(n - 1):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

count = [0 for _ in range(n+1)]

def dfs(node):
    if len(connected[node]) == 1:
        count[node] = 1
        return 1

    if count[node] != 0:
        return count[node]

    count[node] = 1
    for n in connected[node]:
        if count[n] == 0:
            count[node] += dfs(n)

    return count[node]


dfs(r)
for _ in range(q):
    c = int(input())
    print(count[c])
