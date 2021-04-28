import copy
import sys
input = sys.stdin.readline


n, k = map(int, input().split())

def placable(board, pos, size, right):
  y = pos // n
  x = pos % n
  
  for i in range(size):
    cy = y + i if not right else y
    cx = x + i if right else x

    if cy >= n or cx >= n: 
      return False

    c = board[cy][cx]
    if not (c == '.' or c == 'O'):
      return False

  return True

def place(board, pos, size, right):
  y = pos // n
  x = pos % n
  
  for i in range(size):
    cy = y + i if not right else y
    cx = x + i if right else x
    board[cy][cx] = '1'

def is_legal(board):
  for i in range(n):
    for j in range(n):
      if board[i][j] == 'O':
        return False
  return True

def dfs (board, found, pos, rest):
  if len(rest) == 0:
    if is_legal(board):
      return 1
    return 0
  
  if pos >= n*n:
    return 0

  y = pos // n
  x = pos % n
  count = 0
  for size in rest:
    checks = [True, False] if size > 1 else [True]
    for right in checks:
      if placable(board, pos, size, right):
        new_board = copy.deepcopy(board)
        place(new_board, pos, size, right)
        new_rest = copy.deepcopy(rest)
        new_rest.remove(size)
        count += dfs(new_board,found, pos+1, new_rest)
  
  count += dfs(board, found, pos+1, rest)

  return count

board = []
found = []
sizes = []
for i in range (n):
  board.append([])
  s = input()
  for j in range(len(s)):
    board[-1].append(s[j])
    if s[j] == 'O':
      found.append(i*n+j)

for i in range(k):
  sizes.append(int(input()))

answer = dfs(board, found, 0, sizes)

print(answer)