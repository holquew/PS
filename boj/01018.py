
# white == 0, black == 1
def color_diff(start_color, board):
    diff = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i + j) % 2 == start_color:
                if board[i][j] == 'B':
                    diff += 1
            else:
                if board[i][j] == 'W':
                    diff += 1

    return diff


n, m = map(int, input().split())
board = [[None] for _ in range(n)]

for i in range(n):
    board[i] = list(input())

min_diff = n*m
for i in range(n):
    for j in range(m):
        if j + 8 <= m and i + 8 <= n:
            sliced_board = [row[j: j+8] for row in board[i: i+8]]
            temp_min = min(color_diff(0, sliced_board),
                           color_diff(1, sliced_board))
            if min_diff > temp_min:
                min_diff = temp_min

print(min_diff)
