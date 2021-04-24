'''숨바꼭질 3'''
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

MAX = 200000
visited = [False] * MAX
dist = [-1] * MAX
dist[n] = 0
def bfs(s): 
    q = deque([s])
    visited[s] = True
    while q: 
        pop = q.popleft()
        if 0 <= pop*2 < MAX and not visited[pop * 2]: 
            visited[pop*2] = True
            dist[pop*2] = dist[pop]
            q.appendleft(pop*2)

        for new in (pop+1, pop-1):
            if 0 <= new < MAX and not visited[new]: 
                visited[new] = True
                dist[new] = dist[pop] + 1
                q.append(new)       

bfs(n)
print(dist[k])