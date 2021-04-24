import sys
from collections import deque
input = sys.stdin.readline

s = int(input())
def bfs(num, clip):
    q = deque([(num, clip)])
    visited = [[0] * 2000 for _ in range(2000)]
    visited[num][clip] = 0
    while q: 
        screen, board = q.popleft()
        if screen == s: 
            print(visited[screen][board])
            return
        for ns, nb in [(screen, screen), (screen+board, board), (screen-1, board)]: 
            if 0 <= ns < 2000 and nb < 2000 and visited[ns][nb] == 0: 
                visited[ns][nb] = visited[screen][board] + 1
                q.append((ns, nb))
        
bfs(1, 0)
