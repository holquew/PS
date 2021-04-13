import sys
input = sys.stdin.readline

n = int(input())
a = [list(input().rstrip()) for _ in range(n)]


def check(board): 
    answer = 1
    for r in range(n): 
        count = 1 
        for c in range(1, n): 
            if board[r][c] == board[r][c-1]: 
                count += 1
            else: 
                count = 1
            
            if count > answer: 
                answer = count

    for c in range(n): 
        count = 1
        for r in range(1, n): 
            if board[r][c] == board[r-1][c]: 
                count += 1 
            else: 
                count = 1
            
            if count > answer: 
                answer = count
    
    return answer

answer = 0
for r in range(n): 
    for c in range(n): 
        if c+1 < n: 
            a[r][c], a[r][c+1] = a[r][c+1], a[r][c]
            temp = check(a)
            if temp > answer: 
                answer = temp
            a[r][c], a[r][c+1] = a[r][c+1], a[r][c]
        
        if r+1 < n: 
            a[r][c], a[r+1][c] = a[r+1][c], a[r][c]
            temp = check(a)
            if temp > answer: 
                answer = temp
            a[r][c], a[r+1][c] = a[r+1][c], a[r][c]

print(answer)