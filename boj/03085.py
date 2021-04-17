'''사탕 게임'''
import sys
input = sys.stdin.readline


def check(n, board):
    max_count = 0
    for i in range(n):
        count = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                count += 1
            else:
                count = 1
            
            max_count = max(max_count, count)

    for j in range(n):
        count = 1
        for i in range(n-1):
            if board[i][j] == board[i+1][j]:
                count += 1
            else:
                count = 1

            max_count = max(max_count, count)

    return max_count


n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

answer = -1
for r in range(n): 
    for c in range(n):
        if c + 1 < n: 
            board[r][c], board[r][c+1] = board[r][c+1], board[r][c]
            temp = check(n, board)
            answer = max(answer, temp)
            board[r][c], board[r][c+1] = board[r][c+1], board[r][c]
        if r + 1 < n: 
            board[r][c], board[r+1][c] = board[r+1][c], board[r][c]
            temp = check(n, board)
            answer = max(answer, temp)
            board[r][c], board[r+1][c] = board[r+1][c], board[r][c]

print(
    answer
)
