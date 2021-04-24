import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

MAX = 200000
n, k = map(int, input().split())
visited = [0] * (MAX+1)
fro = [None] * (MAX+1)

def bfs(s): 
    q = deque([s])
    while q: 
        pop = q.popleft()
        if pop == k: 
            return visited[pop]
        for new in (pop+1, pop-1, 2*pop):
            if 0 <= new < MAX: 
                if visited[new] == 0: 
                    visited[new] = visited[pop] + 1
                    fro[new] = pop
                    q.append(new)       

answer = bfs(n)
print(answer)
def prnt(n, m):
    if n != m: 
        prnt(n, fro[m])
    print(m, end=' ')

prnt(n, k)