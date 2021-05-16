import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sr, sc, sd = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
count = 0

# 0-N, 1-E, 2-S, 3-W
dr = {3: (0, -1), 0: (-1, 0), 1: (0, 1), 2: (1, 0)}

def turn_left(nd): 
    return (nd+3) % 4

r, c, d = sr, sc, sd
end = False
while not end: 
    # print((r, c))
    if a[r][c] == 0: 
        a[r][c] = 2
        count += 1 
    
    nr, nc = r, c
    for i in range(4): 
        d = (d+3) % 4
        nr, nc = r + dr[d][0], c + dr[d][1]
        if 0 <= nr < n and 0 <= nc < m and a[nr][nc] == 0: 
            r, c = nr, nc
            break
    else: 
        nr, nc = r + dr[(d+2)%4][0], c + dr[(d+2)%4][1]
        if 0 <= nr < n and 0 <= nc < m and a[nr][nc] != 1:
            r, c = nr, nc  
        else: 
            end = True


print(count)