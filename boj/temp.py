from collections import deque

u = (-1, 0)
r = (0, 1)
d = (1, 0)
l = (0, -1)
GO = [[r, r], [l, l], [u, u], [d, d],
     [u, r], [u, l], [r, u], [r, d], 
     [d, r], [d, l], [l, u], [l, d]]

def solution(places):
    n = len(places[0])
    answer = []
    def bfs(board, sr, sc):
        q = deque([(sr, sc)])
        while q: 
            row, col = q.popleft()
            # g = [(0, 1), (0, 1)]
            for g in GO:
                nr, nc = row, col
                for cord in g: 
                    nr += cord[0]
                    nc += cord[1]
                    if 0 <= nr < n and 0 <= nc < n:
                        if board[nr][nc] == 'X':
                            break
                        if board[nr][nc] == 'P':
                            return False
        
        return True 
                
    for place in places: 
        good = True
        for i in range(n):
            for j in range(n):
                if place[i][j] == 'P':
                    print((i, j))
                    if bfs(place, i, j) == False: 
                        good = False
                        break
        if good:
            answer.append(1)
        else: 
            answer.append(0)
    
    return answer

print(
    solution(
        [["PXX", "XPO", "OOO"]]
    )
)