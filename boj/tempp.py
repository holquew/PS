from collections import deque
import heapq

# def solution(board):
#     answer = 0
#     n = len(board[0])

#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     def bfs():
#         dp = [[None] * n for _ in range(n)]
#         dp[0][0] = 0
#         q = [(0, None, 0, 0)]
#         heapq.heapify(q)
#         while q:
#             cost, direction, r, c = q.pop(0)
#             for i in range(len(dr)):
#                 nr, nc = r + dr[i], c + dc[i]
#                 if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
#                     if dp[nr][nc] == None:
#                         new_cost = cost + (100 if direction == None or i == direction else 600)
#                         heapq.heappush(q, (new_cost, i, nr, nc))
#                         dp[nr][nc] = new_cost
#         for i in dp: 
#             print(i)
#         return dp[n-1][n-1]

#     return bfs() 

def solution(board):
    answer = 0
    n = len(board[0])

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    def bfs():
        visited = [[None] * n for _ in range(n)]
        visited[0][0] = 0
        q = deque([(0, 0, 0, 0), (1, 0, 0, 0)])
        while q:
            direction, cost, r, c = q.popleft()
            for i in range(len(dr)):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                    new_cost = cost + (100 if i == direction else 600)
                    if not visited[nr][nc] or visited[nr][nc] >= new_cost:
                        q.append((i, new_cost, nr, nc))
                        visited[nr][nc] = new_cost
        
        return visited[n-1][n-1]

    return bfs()    

print(
    solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
)
