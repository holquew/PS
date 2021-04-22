'''ABCDE'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 인접 행렬
adj = [[False] * n for _ in range(n)]
# 간선 리스트
edges = []
# 인접 리스트
g = [[] for _ in range(n)]

for _ in range(m): 
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = True
    edges.append((a, b))
    edges.append((b, a))
    g[a].append(b)
    g[b].append(a)

m *= 2
for i in range(m): 
    for j in range(m): 
        A, B = edges[i]
        C, D = edges[j]
        if A == B or A == C or A == D or B == C or B == D or C == D: 
            continue
        if not adj[B][C]: 
            continue
        for E in g[D]: 
            if A == E or B == E or C == E or D == E: 
                continue
            print(1)
            sys.exit(0)

print(0)


